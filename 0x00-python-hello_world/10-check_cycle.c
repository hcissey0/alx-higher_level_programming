#include "lists.h"

/**
 * check_cycle - checks if a list has a loop
 * @list: the listint to check
 * Return: 0 if there is no loop, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = list;
	slow = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
