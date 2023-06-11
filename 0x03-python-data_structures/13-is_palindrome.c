#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - a function that checks for palindrome in a linked list
 * @head: the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = *head, *back = *head;
	int stack[2048], top = 0;

	if (!head || !(*head))
		return (1);
	while (back && back->next)
	{
		stack[top++] = front->n;
		front = front->next;
		back = back->next->next;
	}
	if (back)
		front = front->next;
	while (front)
	{
		if (front->n != stack[--top])
			return (0);
		front = front->next;
	}
	return (1);
}
