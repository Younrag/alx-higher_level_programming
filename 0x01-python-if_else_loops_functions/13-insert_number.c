#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: singly linked list
 * @number: to add
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *first, *second, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	first = *head;
	if (*head == NULL)
		*head = new;
	else if (first->n > number)
	{
		new->next = first;
		*head = new;
	}
	else
	{
		while (first->next)
		{
			if (first->next->n <= number)
				first = first->next;
			else
			{
				second = new;
				second->next = first->next;
				first->next = second;
			}
		}
	}

	return (new);
}
