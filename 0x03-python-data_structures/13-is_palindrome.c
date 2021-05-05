#include "lists.h"

/**
 *is_palindrome - function in C that checks if a list is a palindrome.
 *
 *@head: double pointer to head
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int arr[1000];
	int i = 0, j = 0;

	if (head == NULL)
		return (0);
	if (!*head || !(*head)->next)
		return (1);
	while (aux)
	{
		arr[i] = aux->n;
		aux = aux->next;
		i++;
	}
	while ( i > j)
	{
		if (arr[j] != arr[i - 1])
			return (0);
		j++;
		i--;
	}
	return (1);
}
