import apache_beam as beam


class RowToDict(beam.PTransform):
    """
    A Beam PTransform that converts each row of a PCollection into a dictionary.
    This transform is used to standardize the format of the data in the PCollection.
    """
    def __init__(self):
        super().__init__()
    
    def expand(self, pcoll):
        return (pcoll
                | 'Convert Row to Dict' >> beam.Map(lambda x: dict(x)))

class StandarizeHeader(beam.PTransform):
    """
    A Beam PTransform that standardizes the header of a PCollection.
    This transform is used to ensure that the header of the data is consistent
    across different datasets.
    """
    def __init__(self):
        super().__init__()
    
    def expand(self, pcoll):
        return (pcoll
                | 'Standardize Header' >> beam.Map(lambda x: {k.lower(): v for k, v in x.items()}))

    