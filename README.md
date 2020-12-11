# Assignment-8-Advanced-Python

## Finite State Machine Program

A finite state machine has an initial state and a set of transition rules to
other states.  The transition is based on the input and the current state.

Given a file in json format like this:

```
{
    "rules": {
        "s0": {"a": "s0", "b": "s1", "c": "s2"},
        "s1": {"a": "s1", "b": "s1", "c": "s1"},
        "s2": {"a": "s2", "b": "s0", "c": "s2"}
    },
    "inputs": ["a", "c", "b", "c", "a", "b", "a", "b", "b", "c"],
    "initial": "s0"
}
```

There are three states here, `s0`, `s1`, `s2` and three possible inputs,
`a`, `b`, `c`.  The initial state is `s0`  In the first step, we look
at the rules for the current state which is `s0`: `{"a": "s0", "b": "s1", "c": "s2"}`.
In the first step the input is `a` so we transition to state `s0`.  Next, our
state is still `s0` but our input is `c` so we transition to `s2`.  Next, our
state is `s2` and our input is `b` so we transition to `s0`.  This process continues
for every input.  Here is a visualization of the process:

```
a : s0 -> s0
c : s0 -> s2
b : s2 -> s0
c : s0 -> s2
a : s2 -> s2
b : s2 -> s0
a : s0 -> s0
b : s0 -> s1
b : s1 -> s1
c : s1 -> s1
```

Implement a program in `solution.py` which loads the file given by the first
user input, and displays the visualization.

Running the program should look like this:

```
$ python3 solution.py auto.json
a : s0 -> s0
c : s0 -> s2
b : s2 -> s0
c : s0 -> s2
a : s2 -> s2
b : s2 -> s0
a : s0 -> s0
b : s0 -> s1
b : s1 -> s1
c : s1 -> s1
```

## Finite State Machine Class

Now, implement a class, `FiniteStateMachine` in `fsm.py` which has
a constructor (`__init__`) which takes two parameters in addition to `self`:
`rules` and `initial`.  The class should have an attribute, `state` which
represents the current state.  The class should have one method, `next`, which
takes one parameter in addition to `self`: `input` and returns the state after
the transition.  Use this class to implement the first program.
