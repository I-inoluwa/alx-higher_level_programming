#include "lists.h"

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: sorted linked list;
 * @number: value of node to be inserted;
 * Return: returns the node, else NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *current = NULL;

	current = *head;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	if (current->n > number)
	{
		node->next = current;
		*head = node;
		return (node);
	}

	while (current->next != NULL)
	{
		if ((current->next)->n > number)
		{
			node->next = current->next;
			current->next = node;
			return (node);
		}
		current = current->next;
	}

	current->next = node;
	return (node);
}
