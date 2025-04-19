# Copyright 2018-2020 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import inspect
#import textwrap
from collections import OrderedDict
import streamlit as st
#import pandas as pd
#import plotly.express as px

from streamlit.logger import get_logger # get_logger = class (?)
import demos_pertanian #import function2 dr file demos_pertanian

LOGGER = get_logger(__name__) # constructor, properties class didefinisikan dalam method yaitu class atribute __name__

# Dictionary of
# demo_name -> (demo_function, demo_description)
DEMOS = OrderedDict(  #membuat objek DEMOS dari class
    [
      ("—", (demos_pertanian.intro, None)),
        (
           "1. Visual Data Padi dan Beras",
            (
                demos_pertanian.padi_visual,
            ),
        ),
        (
            "2. Visual Data Jagung",
            (
                demos_pertanian.jagung_visual,
            ),
        ),            
        (
            "3. Visual Data Cabe Rawit",
            (
                demos_pertanian.caberawit_visual,
            ),
        ),       
        (
            "4. Visual Data Cabe Besar",
            (
                demos_pertanian.cabebesar_visual,
            ),
        ),      
        (
            "5. Visual Data Bawang Merah",
            (
                demos_pertanian.bawangmerah_visual,
            ),
         ),
           (
            "6. Visual Data Bawang Putih",
            (
                demos_pertanian.bawangputih_visual,
            ),
          ),      
    ]
)


def run():
    demo_name = st.sidebar.radio("Pilih Komoditas", list(DEMOS.keys()), 0)
    demo = DEMOS[demo_name][0]

    if demo_name == "—":
#        show_code = False
        st.write("# Selamat datang di Data Visual Pertanian, Kabupaten Malang, Tahun 2019 👋")
    else:
#        show_code = st.sidebar.checkbox("Show code", True)
        st.markdown("# %s" % demo_name)
#        description = DEMOS[demo_name][0]
# =============================================================================
#         if description:
#             st.write(description)
#         # Clear everything from the intro page.
#         # We only have 4 elements in the page so this is intentional overkill.
#         for i in range(10):
#             st.empty()
# =============================================================================

    demo()

#    if show_code:
#        st.markdown("## Code")
#        sourcelines, _ = inspect.getsourcelines(demo)
#        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__": #memanggil method class get_logger
    run() # menjalankan function run()


