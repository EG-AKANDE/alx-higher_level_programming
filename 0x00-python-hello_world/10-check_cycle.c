#include "lists.h"

/**
 * check_cycle - checks for cycle
 * @list: head list pntr
 *
 * Return: 0 if none present, 1 if present
 */

int check_cycle(listint_t *list)

{
	/* introducing floyd */
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
{
	slow = slow->next;
	fast = fast->next->next;

	/* meet means loop */
	if (slow == fast)
	return (1);
}

	/* none loop */
	return (0);
}
