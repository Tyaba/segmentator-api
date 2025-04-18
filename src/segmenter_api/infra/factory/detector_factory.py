from functools import lru_cache

from segmenter_api.domain.factory.detector_factory import (
    DetectorFactoryInterface,
    DetectorType,
)
from segmenter_api.domain.service.detector import Detector
from segmenter_api.infra.service.detector.florence2_detector import (
    Florence2Detector,
)
from segmenter_api.infra.service.detector.grounding_dino import (
    GroundingDinoDetector,
)


class DetectorFactory(DetectorFactoryInterface):
    @lru_cache
    def create(self, detector_type: DetectorType) -> Detector:
        from segmenter_api.di import resolve

        if detector_type == DetectorType.FLORENCE2:
            return resolve(Florence2Detector)
        elif detector_type == DetectorType.GROUNDING_DINO:
            return resolve(GroundingDinoDetector)
        error_msg = f"Invalid detector type: {detector_type}"
        raise ValueError(error_msg)
