
def model(input_shape, dropout=True, l2=True, batch_norm=True):

    layer1 = {  'layer': 'input',
                'input_shape': input_shape
             }
    layer2 = {  'layer': 'conv1d',
                'num_filters': 24,
                'filter_size': 19,
                'padding': 'SAME',
                'activation': 'relu',
                'global_pool': 'max', 
                }
    if batch_norm:
        layer2['norm'] = 'batch'
    layer3 = {  'layer': 'dense',
                'num_units': 96,
                'activation': 'relu',
                }
    if dropout:
        layer3['dropout'] = 0.5
    if batch_norm:
        layer3['norm'] = 'batch'
    layer4 = {  'layer': 'dense',
                'num_units': 1,
                'activation': 'sigmoid',
                }

    model_layers = [layer1, layer2, layer3, layer4]

    # optimization parameters
    optimization = {"objective": "binary",
                  "optimizer": "adam",
                  "learning_rate": 0.0003,
                  }
    if l2:
        optimization['l2'] = 1e-6

    return model_layers, optimization
