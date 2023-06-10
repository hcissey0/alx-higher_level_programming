#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - a function that checks for palindrome in a linked list
 * @head: the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, n = 0;
	listint_t *ptr;
	listint_t *temp;
	listint_t *mid;

	if ((*head) == NULL || head == NULL)
		return (1);
	ptr = (*head);
	temp = (*head);
	mid = (*head);
	while (temp != NULL)
	{
		temp = temp->next;
		n++;
	}
	j = n / 2;
	if (n % 2 != 0)
		j+= 1;
	while (i++ < j)
		mid = mid->next;
	for (i = 0; i < n / 2; i++)
	{
		temp = mid;
		for (j = 0; j < (n / 2) - (i + 1); j++)
			temp = temp->next;
		if (ptr->n != temp->n)
			return (0);
		ptr = ptr->next;
	}
	return (1);
}
