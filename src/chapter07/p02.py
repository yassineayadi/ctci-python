"""
**Call Center**:

Imagine you have a call center with three levels of employees: respondent, manager, and director.
An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call,
he or she must escalate the call to a manager. If the manager is not free or not able to handle it, then the call should
be escalated to a director. Design the classes and data structures for this problem.

Implement a method dispatchCall() which assigns a call to the first available employee.

"""


from dataclasses import dataclass
from enum import Enum
from typing import List


class State(Enum):
    busy = "busy"
    free = "free"


class Priority(Enum):
    low = 1
    medium = 2
    high = 3


@dataclass
class Call:
    priority = Priority

    def route_to(self, employee: "Employee"):
        employee.call = self

    def increase_priority(self):
        if self.priority == Priority.low:
            self.priority = Priority.medium
        elif self.priority == Priority.medium:
            self.priority = Priority.high


@dataclass
class Employee:
    state: State
    call: Call

    def escalate_call(self):
        if self.call:
            self.call.increase_priority()


@dataclass
class Manager(Employee):
    pass


@dataclass
class Director(Employee):
    pass


@dataclass
class CallQueue:
    queue: List[Call]
    respondents: List[Employee]

    def register_call(self, call: Call):
        self.queue.append(call)

    def dispatch_call(self):
        call = self.queue.pop(0)
        next_respondent = self.respondents.pop(0)
        call.route_to(next_respondent)


class MangerCallQueue:
    respondents: List[Manager]


class DirectorCallQueue:
    respondents: List[Director]
