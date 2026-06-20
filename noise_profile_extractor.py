import numpy as np
import csv
import os

# --- DEFINE CONSTANT PATH HERE ---
# Modify this path to match your local system environment
SAVE_PATH = r"./System_Modelling_Output"

def get_noise_profile(f_vec, icp_designed=1e-3, f_ref=160e6):
    I_ref = 300e-6
    
    # Noise floor and profile calculations
    s_vco = 10 * np.log10(((1e6 / f_vec)**2) * 10**(-115 / 10) + 10**(-145 / 10))
    s_ref = 10 * np.log10(((100e3 / f_vec)**2) * 10**(-139 / 10) + 10**(-150 / 10))
    
    pn_norm = -231
    cp_floor_actual = pn_norm + 10 * np.log10(icp_designed / I_ref)
    s_cp = 10 * np.log10((2e6 / f_vec) * 10**(cp_floor_actual / 10) + 10**(cp_floor_actual / 10))
    
    def digital_pn(floor):
        return 10 * np.log10((2e6 / f_vec) * 10**(floor / 10) + 10**(floor / 10))
    
    s_div_n, s_div_r, s_div_p, s_buffer = [digital_pn(-160) for _ in range(4)]

    # --- SAVING LOGIC ---
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    full_filename = os.path.join(SAVE_PATH, 'pll_raw_noise_profiles.csv')

    header = ['Frequency_Hz', 'Reference_dBc_Hz', 'VCO_dBc_Hz', 'ChargePump_dBc_Hz', 
              'N_Divider_dBc_Hz', 'R_Divider_dBc_Hz', 'P_Divider_dBc_Hz', 'Buffer_dBc_Hz']

    with open(full_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in zip(f_vec, s_ref, s_vco, s_cp, s_div_n, s_div_r, s_div_p, s_buffer):
            writer.writerow(row)
    
    print(f"SUCCESS: Phase noise profiles saved at: {full_filename}")

if __name__ == "__main__":
    # Generate frequency vector from 10 Hz to 100 MHz
    f_log = np.logspace(1, 8, 1000)
    get_noise_profile(f_log)
