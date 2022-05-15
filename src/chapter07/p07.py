"""
**Chat Server:**

Explain how you would design a chat server. In particular, provide details about the various backend components, classes,
and methods. What would be the hardest problems to solve?
"""

# Objects
# * User
# * Roles
# * Message (Private/Room)
# * Room
# * Room Rules
# * Index

# Description:
# * Each room has at least 1 admin
# * User can have multiple roles which will grant them different levels of permissions
# * Messages can be sent privately or within a room
# * Room can have rules (e.g. length of the message number of messages)
# * Message could support markup languages

# Actions:
# * Send Message
# * Connect to Room (can connect to multiple rooms)
# * Administer Room (ban user/grant rights)

# BackEnd:
# * Application Server (to manage the application logic)
# * Webserver (to manage incoming HTTP requests)
# * Database (if messages need to be store otherwise no database)
# * User Authentication (require username/password)
# * Websockets to broadcast messages or Ajax to pull/push latest messages

# What would be the hardest problem?
# (1) Scaling, and redundancy
# We want to make sure that we have multiple servers/VMs responsible for a part of the system
# E.g. for user management/authentication (we do not want 1 point of failure). Having only 1 database could also be a problem if we reach concurrency bottlenecks.
# We want to have either json-based database which enables us to partition the data. Or we could alternatively use sharding with a Postgres DB with some replication across multiple nodes.
# E.g. we could a kunernetes cluster to manage multiple instance of the same program.

# (2) If we start scaling and splitting items we need a way to make sure data syncs.
# just simple have the server be the source of truth

# (3) Managing good behaviour (We want to avoid be DDOSed).
# We could implement throttling/rate limiting on individual users.

# (4) When is a user really online?
# If we just rely on HTTP the protocal is stateless. Or how do we handle users timing out. Should the client ping the server at regular intervals?


from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Union


class UserStatus(Enum):
    ONLINE = "Online"
    OFFLINE = "Offline"
    AWAY = "Away"
    BUSY = "Busy"


class FriendRequestStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


@dataclass
class FriendRequest:
    sender: "User"
    receiver: "User"
    status: FriendRequestStatus = field(default=FriendRequestStatus.PENDING)

    def accept(self):
        self.status = FriendRequestStatus.ACCEPTED

    def add_friend(self):
        self.sender.friends.append(self.receiver)
        self.receiver.friends.append(self.sender)

    def reject(self):
        self.status = FriendRequestStatus.REJECTED


@dataclass
class AuthenticationMixin:
    authenticated: bool
    hashed_password: str


@dataclass
class User(AuthenticationMixin):
    name: str
    friends: List["User"]
    rooms: List["Room"]
    conversations: Dict["User", "Conversation"]
    status: UserStatus
    user_manager: "UserManager"
    received_friend_requests: Dict["User", FriendRequest]
    sent_friend_requests: Dict["User", FriendRequest]

    def join_room(self, room: "Room"):
        if room not in self.rooms:
            self.rooms.append(room)
            room.users.append(self)

    def send_friend_request(self, receiver: "User"):
        friend_request = FriendRequest(self, receiver)
        self.user_manager.send_friend_request(friend_request, receiver)

    def receive_friend_request(self, friend_request: "FriendRequest"):
        sender = friend_request.sender
        self.received_friend_requests[sender] = friend_request

    def accept_friend_request(self, sender: "User"):
        friend_request = self.received_friend_requests[sender]
        friend_request.accept()

    def reject_friend_request(self, sender: "User"):
        friend_request = self.received_friend_requests[sender]
        friend_request.reject()

    def send_message_to(self, text: str, receiver: Union["Room", "User"]):
        message = Message(text, sender=self, receiver=receiver)
        receiver.receive_message(message)

    def receive_message(self, message: "Message"):
        sender = message.sender
        if sender not in self.conversations:
            conversation = Conversation([self, sender], [message])
            self.conversations[sender] = conversation
        else:
            self.conversations[sender].messages.append(message)


@dataclass
class UserManager:
    users: Dict[str, "User"]

    def login(self, username: str, hashed_password: str):
        if username in self.users and self.users[username] == hashed_password:
            user = self.users[username]
            user.authenticated = True
            user.user_manager = self
        else:
            print("Incorrect credentials.")

    @staticmethod
    def send_friend_request(friend_request: FriendRequest, receiver: User):
        receiver.receive_friend_request(friend_request)


@dataclass
class Conversation:
    users: List["User"]
    messages: List["Message"]


@dataclass
class Message:
    text: str
    sender: "User"
    receiver: Union["User", "Room"]
    limit: int = 140


@dataclass
class Room(Conversation):
    Admins: List["User"]

    def receive_message(self, message: "Message"):
        self.messages.append(message)
