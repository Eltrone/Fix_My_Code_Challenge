#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current = *head;
	dlistint_t *temp = NULL;
	unsigned int i = 0;

	if (*head == NULL) /* Liste vide */
	{
		return (-1);
	}

	if (index == 0) /* Suppression du premier nœud */
	{
		temp = *head;
		*head = (*head)->next;
		if (*head != NULL) /* Si la liste contient plus d'un nœud */
		{
			(*head)->prev = NULL;
		}
		free(temp);
		return (1);
	}

	while (i < index && current != NULL) /* Parcours jusqu'à l'index */
	{
		current = current->next;
		i++;
	}

	if (current == NULL) /* Index hors de la portée */
	{
		return (-1);
	}

	if (current->next != NULL) /* Si le nœud à supprimer n'est pas le dernier */
	{
		current->next->prev = current->prev;
	}

	if (current->prev != NULL) /* Si le nœud à supprimer n'est pas le premier */
	{
		current->prev->next = current->next;
	}

	free(current); /* Libère la mémoire du nœud à supprimer */

	return (1);
}
