#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle;
 * @list: linked list to be checked;
 * Return: returns (1) on true and (0) on false.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	while (fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == NULL)
			break;

		if (slow == fast)
			return (1);
	}

	return (0);
}
