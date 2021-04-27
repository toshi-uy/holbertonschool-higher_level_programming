#include "lists.h"
#include <stdlib.h>

/**
 * print_listint - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: number to add
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *aux = NULL;
	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	aux = *head;
	if (aux->n > number)
	{
		new->next = aux;
		*head = new;
		return (new);
	}
	else
	{
		while (aux->next)
		{
			if (aux->n <= number && aux->next->n >= number)
			{
				new->next = aux->next;
				aux->next = new;
				return (new);
			}
			aux = aux->next;
		}
		aux->next = new;
	}
	return (new);
}
