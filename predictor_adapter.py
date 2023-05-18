import predictor
import network_classes as nn_classes
from predictor_types import Predictor_types

linear_rel_predictor = predictor.Predictor("linear_rel", nn_classes.linear_net_06_05, conv_factor=False)

conv_abs_predictor = predictor.Predictor("conv_abs", nn_classes.conv2d_net_06_05, conv_factor=True)

conv_rel_predictor = predictor.Predictor("conv_rel", nn_classes.conv2d_net_06_05, conv_factor=True)

predictor_to_object = {
    Predictor_types.LINEAR_REL_PREDICTOR: linear_rel_predictor,
    Predictor_types.CONV_ABS_PREDICTOR: conv_abs_predictor,
    Predictor_types.CONV_REL_PREDICTOR: conv_rel_predictor,
}

predictor_to_dna_analisys_type = {
    Predictor_types.LINEAR_REL_PREDICTOR: predictor.Processing.NN,
    Predictor_types.CONV_ABS_PREDICTOR: predictor.Processing.D2,
    Predictor_types.CONV_REL_PREDICTOR: predictor.Processing.D2
}


