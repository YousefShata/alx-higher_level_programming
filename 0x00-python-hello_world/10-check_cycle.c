#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to head
 * Return:  0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *end, *start;
	if (list == NULL)
		return (0);
	start = list;
	end = list->next;
	if (end == NULL)
	return (0);
	
	while (start != end)
	{
		if (end->next == NULL || end->next->next == NULL)
			return (0);
		start = start->next;
		end = end->next->next;
	}
	return (1);
}
