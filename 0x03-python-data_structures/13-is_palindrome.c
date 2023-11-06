#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);

/**
 * is_palindrome - function that checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int is_palindrome(listint_t** head)
{
	listint_t* slow = *head;
	listint_t* fast = *head;
	listint_t* firstHalf = *head;
	listint_t* secondHalf = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	secondHalf = reverse_list(slow);

	while (secondHalf != NULL)
	{
		if (firstHalf->data != secondHalf->data)
			return (0);
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}

	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to head of linked list so we can modify it
 *
 */
void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *cur;

	current = *head;
	while (current)
	{
		next = current->next;
		cur->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
