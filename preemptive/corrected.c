#include 

/* Structure definition:
   struct list_s {
       int n;
       struct list_s *next;
   };
   typedef struct list_s list_t;
*/

list_t *add_node_end(list_t *head, const int n) {
    list_t *new_node = malloc(sizeof(list_t));
    if (!new_node)
        return (NULL); // Prevent null pointer dereference on allocation failure

    new_node->n = n;
    new_node->next = NULL;

    // If the list is empty, the new node is the head
    if (!head)
        return (new_node);

    // Traverse to the last node
    list_t *current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    // Correctly link the new node at the end
    current->next = new_node;

    return (head);
}