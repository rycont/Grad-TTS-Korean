from hifi_gan.env import AttrDict
import json
import torch
from models import Generator as HiFiGAN

def get_hifigan():
    with open('./checkpts/hifigan-config.json') as f:
        h = AttrDict(json.load(f))
    hifigan = HiFiGAN(h)
    hifigan.load_state_dict(torch.load('./checkpts/hifigan.pt', map_location=lambda loc, storage: loc)['generator'])
    _ = hifigan.cuda().eval()

    hifigan.remove_weight_norm()

    return hifigan