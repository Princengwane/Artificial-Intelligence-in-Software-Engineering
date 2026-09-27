AI: Preemptive Bug Fixing
This folder contains the deliverables, code artifacts, and documentation for the Preemptive Bug Fixing AI Lab Assignment. The objective of this task is to utilize a structured, role-based AI prompt to conduct a comprehensive code review of a vulnerable C function, identify logical flaws and memory safety risks, and implement a robust, production-ready fix.

Code Review & Vulnerability Summary
Correctness & Logical Linking Error
The Flaw: In the original add_node_end implementation, the while (current) loop traversed until current fell off the end of the list (NULL).
The Issue: Reassigning current = new_node; only updated the local stack variable copy of current rather than modifying the next pointer of the actual last node in the list. This failure in list traversal termination left the new node unlinked and caused the function to return the original head unchanged.
The Fix: Traverse until current->next == NULL so that current stops at the last valid node, allowing direct assignment to current->next = new_node;.
Memory Safety Flaw (malloc Validation)
The Flaw: Memory was allocated for new_node using malloc(sizeof(list_t)) without verifying whether the operation succeeded.
The Issue: If malloc fails under low-memory conditions and returns NULL, subsequent operations like new_node->n = n; attempt to dereference a null pointer, immediately triggering a Segmentation Fault and crashing the application.
The Fix: Introduce an explicit NULL check immediately after allocation to handle system resource exhaustion safely