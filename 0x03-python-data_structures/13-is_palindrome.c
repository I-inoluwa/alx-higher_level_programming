#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome;
 * @head: linked list to be checked;
 * Return: returns (1) if list is a palindrome, and (0) otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = NULL, *pal = NULL, *new = NULL, *fast = NULL;

	if (*head == NULL)
		return (1);

	cur = *head, fast = *head;
	while (fast != NULL)
	{
		if (fast->next == NULL)
			break;
		fast = fast->next->next;
		cur = cur->next;
	}
	while (cur != NULL)
	{
		pal = malloc(sizeof(listint_t));
		if (pal == NULL)
			return (0);
		pal->n = cur->n;
		pal->next = NULL;

		cur = cur->next;
		if (new != NULL)
			pal->next = new;
		new = pal;
	}
	cur = *head;
	while (pal != NULL)
	{
		if (cur->n != pal->n)
		{
			free_listint(new);
			return (0);
		}
		cur = cur->next;
		pal = pal->next;
	}
	free_listint(new);
	return (1);
}
