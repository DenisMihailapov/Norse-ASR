import torch
import numpy as np
import pandas as pd

import cochlea
import thorns as th



class SpikeUtils():

    def __init__(self, newron_in_layer: int, count_classes:int, species= 'human'):
        self.count_classes = count_classes
        self.newron_in_layer = newron_in_layer
        if not species in ['human', 'cat']: raise ValueError('species must be \'human\' or \'cat\'') 
        self.species= species

    def get_targ_other_decired_ST(self, len_train: int):
        ost = len_train%10
        len_train = len_train//10


        times_mid = int((len_train*0.3))
        des_spikes_40_per = torch.tensor([0, 0, 0, 1, 1, 0, 0, 0, 1, 1 ]).repeat(times_mid)
        des_spikes_60_per = torch.tensor([0, 0, 1, 0, 0, 1, 0, 1, 0, 0]).repeat(times_mid)

        times_post = int((len_train*0.2))
        des_spikes_ones = torch.tensor([1, 0, 1, 0, 1]).repeat(2*times_post)


        times_pre  = len_train - (2*times_mid + times_post)
        des_spikes_zeros = torch.tensor([0, 0, 0, 0, 0]).repeat(2*times_pre)


        target_train = torch.cat((torch.zeros(ost),
                                des_spikes_zeros, 
                                des_spikes_40_per, 
                                des_spikes_60_per,
                                des_spikes_ones), 0)

        other_train = torch.cat((torch.zeros(ost),
                                des_spikes_zeros, 
                                des_spikes_40_per, 
                                des_spikes_40_per,
                                torch.zeros(times_post*10)), 0)

        return target_train, other_train

    def get_disired_spike_array(self, len_train: int, digit:int):
        if not digit in range(self.count_classes): return None

        target_train, other_train = self.get_targ_other_decired_ST(len_train)

        arr = torch.zeros((self.count_classes, len(target_train)))
        for i in range(self.count_classes):
            arr[i] = other_train
        arr[digit] = target_train

        return arr

    def audio_to_spike_train(self, audio, fs = 100e3):
        return cochlea.run_zilany2014(
            audio.astype(np.float64), fs,
            anf_num=(self.newron_in_layer, 0, 0),
            cf=10000, seed=0,
            species= self.species
        ).loc[:, 'spikes':'duration'] # without cf and type

    def audio_to_spike_array(self, audio, fs = 100e3):

        spike_array = th.trains_to_array(self.audio_to_spike_train(audio, fs), fs)

        return torch.tensor(spike_array, dtype=torch.float, device=torch.device('cuda'))

    def array_to_trains(self, arrs, fs = 100e3):
        trains = []
        for j in range(len(arrs[0])):
            trains.append([])
            for i in range(len(arrs)):
                if arrs[i][j] == 1:
                    trains[-1].append(i/fs)
             
        return pd.DataFrame(list(zip(trains, [len(arrs)/fs]*len(arrs[0]))), columns =['spikes', 'duration'])    
    
    def trains_to_array(self, train, fs = 100e3):
        return th.trains_to_array(train, fs)
 
    def plot_audio_in_trains(self, audio, fs = 100e3):
        th.plot_raster(self.audio_to_spike_train(audio, fs)) 
    
    def plot_spike_array_in_trains(self, spike_array, fs = 100e3):
        th.plot_raster(self.array_to_trains(spike_array, fs))     

