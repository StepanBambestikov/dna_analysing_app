import predictor
import network_classes as nn_classes
from predictor_types import Predictor_types

linear_predictor = predictor.Predictor(nn_classes.multi_nn_2layer_net, conv_factor=False,
                                       dna_process_manager=predictor.dna_handlers[predictor.Processing.D2])

test_predictor = predictor.Predictor(predictor.make_test_network, conv_factor=False,
                                     dna_process_manager=predictor.dna_handlers[predictor.Processing.D2])

predictor_to_object = {
    Predictor_types.LINEAR_PREDICTOR: linear_predictor,
    Predictor_types.TEST_PREDICTOR: test_predictor
}
