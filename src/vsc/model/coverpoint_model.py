#   Copyright 2019 Matthew Ballance
#   All Rights Reserved Worldwide
#
#   Licensed under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in
#   compliance with the License.  You may obtain a copy of
#   the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in
#   writing, software distributed under the License is
#   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#   CONDITIONS OF ANY KIND, either express or implied.  See
#   the License for the specific language governing
#   permissions and limitations under the License.

'''
Created on Aug 3, 2019

@author: ballance
'''

class CoverpointModel():
    
    def __init__(self, cp, name, bin_model_l):
        self.cp = cp
        self.name = name
        self.bin_model_l = bin_model_l
       
        self.n_bins = 0
        for b in self.bin_model_l:
            self.n_bins += b.get_n_bins()
        
    def sample(self):
        for b in self.bin_model_l:
            b.sample()

    def accept(self, v):
        v.visit_coverpoint(self)
            
    def dump(self, ind=""):
        print(ind + "Coverpoint: " + self.name)
        for b in self.bin_model_l:
            b.dump(ind + "    ")
            
    def get_n_bins(self):
        return self.n_bins
        
    def get_bin_hits(self, bin_idx):
        b = None
        for i in range(len(self.bin_model_l)):
            b = self.bin_model_l[i]
            if b.get_n_bins() > bin_idx:
                break
            bin_idx -= b.get_n_bins()
            
        return b.get_hits(bin_idx)
    
    def get_hit_bins(self, bin_l):
        bin_idx = 0
        for bin in self.bin_model_l:
            if bin.hit_idx() != -1:
                bin_l.append(bin_idx + bin.hit_idx())
            bin_idx += bin.n_bins()
        
        