"""
Classifier Service
Implements k-Nearest Neighbors algorithm for species classification
"""
import math
from domain.penguin import Penguin
from domain.exceptions import NoDataLoadedException, EmptyDatasetException
from repository.penguin_repo import PenguinRepo


class ClassifierService:
    def __init__(self, penguin_repo: PenguinRepo):
        self.__penguin_repo = penguin_repo

    def _check_data_loaded(self):
        """Check if data is loaded"""
        if self.__penguin_repo.get_penguin_count() == 0:
            raise NoDataLoadedException()

    def _euclidean_distance(self, p1: tuple, p2: tuple) -> float:
        """
        Calculate Euclidean distance between two points
        :param p1: tuple of (culmen_len, culmen_depth, flipper_len)
        :param p2: tuple of (culmen_len, culmen_depth, flipper_len)
        :return: distance
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

    def classify(self, culmen_len: float, culmen_depth: float, flipper_len: float, k: int) -> str:
        """
        Classify a penguin species using k-Nearest Neighbors algorithm
        
        Time Complexity: O(n log n) for sorting distances, O(n) for distance calculation
        Space Complexity: O(n) for storing distances
        
        :param culmen_len: culmen length in mm
        :param culmen_depth: culmen depth in mm
        :param flipper_len: flipper length in mm
        :param k: number of nearest neighbors
        :return: predicted species
        :raises NoDataLoadedException if no data loaded
        """
        self._check_data_loaded()

        penguins = self.__penguin_repo.get_all_penguins()
        if not penguins:
            raise EmptyDatasetException()

        # Calculate distances to all penguins
        point = (culmen_len, culmen_depth, flipper_len)
        distances = []

        for penguin in penguins:
            penguin_point = (
                penguin.get_culmen_length_mm(),
                penguin.get_culmen_depth_mm(),
                penguin.get_flipper_length_mm()
            )
            dist = self._euclidean_distance(point, penguin_point)
            distances.append((dist, penguin.get_species()))

        # Sort by distance and get k nearest
        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:min(k, len(distances))]

        # Vote for species
        votes = {}
        for dist, species in k_nearest:
            votes[species] = votes.get(species, 0) + 1

        # Return species with most votes
        predicted_species = max(votes, key=votes.get)
        return predicted_species

    def classify_with_details(self, culmen_len: float, culmen_depth: float, 
                             flipper_len: float, k: int) -> dict:
        """
        Classify with detailed results including confidence
        :return: dictionary with prediction and details
        """
        self._check_data_loaded()

        penguins = self.__penguin_repo.get_all_penguins()
        if not penguins:
            raise EmptyDatasetException()

        point = (culmen_len, culmen_depth, flipper_len)
        distances = []

        for penguin in penguins:
            penguin_point = (
                penguin.get_culmen_length_mm(),
                penguin.get_culmen_depth_mm(),
                penguin.get_flipper_length_mm()
            )
            dist = self._euclidean_distance(point, penguin_point)
            distances.append((dist, penguin.get_species()))

        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:min(k, len(distances))]

        votes = {}
        for dist, species in k_nearest:
            votes[species] = votes.get(species, 0) + 1

        predicted_species = max(votes, key=votes.get)
        confidence = votes[predicted_species] / len(k_nearest) * 100

        return {
            'prediction': predicted_species,
            'confidence': round(confidence, 2),
            'votes': votes,
            'k_used': len(k_nearest)
        }
