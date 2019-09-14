import numpy

class IntervalTree:
    """Interval Tree Implementation

    Supports the following queries:
    find all intervals fully contained in a query interval
    find all intervals partially contained in a query interval
    find all intervals that contain a query interval
    find the minium bounding box that fully contains all intervals
    find the minimum bounding box that partially contains all intervals
    """

    def __init__(self, num_dimensions=1, intervals=None):
        self.dims = num_dimensions
        if (not intervals):
            self.root = None
        else:
            self.root = self.add_intervals(intervals)


    def is_overlapping(self):
        """Determines if any of the intervals in the tree are overlapping"""

    def add(self, intervals):
        """Adds intervals

        Args:
            intervals: A list of tuples (min_bound, max_bound), where min_bound and
            max_bound is an array of length N denoting the min and max bounds of the
            interval.

        Raises:
            Wrong Dimension: If at least one of the intervals' dimension is not consistent
            with self.dims
        """


    def remove(self, interval):
        """Removes an interval

        Args: interval: the interval to remove

        Raises:
            Interval Does Not Exist: If the interval does not exist
        """

    def is_contained(self, interval, type_="full"):
        """Determines if the interval is contained in any interval
    
        Args:
            interval: the interval
            type_ (optional): ('full' | 'partial') - specify the type of containment

        Returns:
            A bool indicating whether or not the interval is contained in some interval in the tree
        """

    def contained_in(self, interval, type_="full"):
        """Gets all the intervals contained in interval

        Args:
            interval: the interval
            type_ (optional): ('full' | 'partial') - specify the type of containment

        Returns:
            A list of all intervals contained in interval
        """

    def containing(self, interval, type_="full"):
        """Gets all the intervals that contain interval

        Args:
            interval: the interval
            type_ (optional): ('full' | 'partial') - specify the type of containment

        Returns:
            A list of all intervals containing interval
        """


    def min_bounding_box(self, type_="full"):
        """Gets the minimum bounding interval that contains the intervals in the tree
        
        Args:
            type_ (optional): ('full' | 'partial') - specify the type of containment

        Returns: A tuple (min_bound, max_bound) denoting the bounding box
        """
        pass

    def partial_bbox(self):
        """Gets the minimum bounding interval that partially contains all the intervals

        Returns: A tuple (min_bound, max_bound) denoting the bounding box
        """
        pass


