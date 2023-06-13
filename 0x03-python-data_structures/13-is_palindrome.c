#include "lists.h"
#include <stddef.h>

listint_t *reverse_linked_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_linked_list - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_linked_list(listint_t **head)
{
listint_t *current_node = *head, *next_node, *previous_node = NULL;

while (current_node)
{
next_node = current_node->next;
current_node->next = previous_node;
previous_node = current_node;
current_node = next_node;
}

*head = previous_node;
return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *temp, *reversed, *middle;
size_t list_size = 0, index;

if (*head == NULL || (*head)->next == NULL)
return (1);

temp = *head;
while (temp)
{
list_size++;
temp = temp->next;
}

temp = *head;
for (index = 0; index < (list_size / 2) - 1; index++)
temp = temp->next;

if ((list_size % 2) == 0 && temp->n != temp->next->n)
return (0);

temp = temp->next->next;
reversed = reverse_linked_list(&temp);
middle = reversed;

temp = *head;
while (reversed)
{
if (temp->n != reversed->n)
return (0);
temp = temp->next;
reversed = reversed->next;
}
reverse_linked_list(&middle);

return (1);
}
