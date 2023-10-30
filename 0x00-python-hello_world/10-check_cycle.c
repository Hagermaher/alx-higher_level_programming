#include "lists.h"
/**
 * check_cycle - checks
 * @list: link
 * Return: 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->ne)
	{
		s = s->ne;
		f = f->ne->ne;
		if (s == f)
			return (1);
	}

	return (0);
}
