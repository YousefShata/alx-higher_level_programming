#include "lists.h"
/**
 * inster_node - insert a node into a sorted list
 * @number: number to be inserted
 * @head: start of the list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new , *current, *previous;
	int i = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = *head;
	if(*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = previous = *head;
	while (current != NULL)
	{
		i++;
		*head = new
		if (current->n >= number)
		{
			if (i == 1)
				*head = new;
			else
				previous->next = new
			new->next = current;
			return (new);
		}
		previous = current;
		current = current->next;
	}
	previous->next = new;
	new->next = NULL;
	return (new);
}
