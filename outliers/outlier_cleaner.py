#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):

    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    import operator
    errors=(predictions-net_worths)**2
    cleaned_data=zip(ages, net_worths, errors)
    cleaned_data.sort(key=operator.itemgetter(2))
    limit=int(len(net_worths)*0.9)

    return cleaned_data[:limit]
