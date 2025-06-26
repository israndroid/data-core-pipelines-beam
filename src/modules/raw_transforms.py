import apache_beam as beam


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

    