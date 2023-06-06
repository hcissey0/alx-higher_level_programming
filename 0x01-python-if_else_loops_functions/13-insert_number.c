#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in an ordered linked list
 * @head: pointer to pointer of the list
 * @number: the number to insert
 * Return: the address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (current)
	{
		if (current->n == new->n)
		{
			temp = current->next;
			current->next = new;
			new->next = temp;
			return (new);
		}
		else if (current->n > new->n)
			break;
		else
		{
			temp = current;
			current = current->next;
		}
	}
	if (current == NULL)
		current = new;
	else
	{
		temp->next = new;
		new->next = current;
	}
	return (new);
}
