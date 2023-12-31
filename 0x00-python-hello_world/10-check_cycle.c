#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks
 * @list: link
 * Return: 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (list == NULL || list->ne == NULL)
		return (0);

	s = list->ne;
	f = list->ne->ne;

	while (s && f && f->ne)
	{
		if (s == f)
			return (1);


		s = s->ne;
		f = f->ne->ne;
	}

	return (0);
}
