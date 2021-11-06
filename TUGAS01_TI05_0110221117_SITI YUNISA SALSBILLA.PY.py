Pegawai = 'Ahmad'
Agama = 'Muslim' 
GajiPokok = 4000000
Anak = 2
TunjanganJabatan= 0.2 * GajiPokok 

if (Anak <= 2): 
    TunjanganKeluarga = 0.10 * GajiPokok
elif (Anak >= 2):
    TunjanganKeluarga = 0.20 * GajiPokok
else: 
    TunjanganKeluarga = 0

GajiKotor = GajiPokok + TunjanganJabatan + TunjanganKeluarga
ZakatProfesi = (0, 0.025)[Agama == 'Muslim' and GajiKotor >= 6000000]
GajiBersih = GajiKotor - ZakatProfesi

print(
    '_ _ _ _ _ _ _ _ _ _ _ _'
    '\nSLIP GAJI PT. Renalmed'
    '\nNama Pegawai\t\t :', Pegawai,
    '\nAgama\t\t\t :', Agama, 
    '\nJumlah Anak\t\t :', Anak,
    '\nGaji Pokok\t\t :Rp.', GajiPokok,
    '\nTunjangan Jabatan\t :Rp.', TunjanganJabatan,
    '\nTunjangan Keluarga\t :Rp.', TunjanganKeluarga,
    '\nGaji Kotor\t\t :Rp.', GajiKotor,
    '\nZakat Profesi\t\t :Rp.', ZakatProfesi,
    '\nTake Home\t\t :Rp.', GajiBersih
)

Pegawai = 'Alex'
Agama = 'Kristen'
GajiPokok = 6000000
Anak = 5
TunjanganJabatan = 0.2 * GajiPokok

if (Anak <= 2):
    TunjanganKeluarga = 0.10 * GajiPokok
elif (Anak >= 2): 
    TunjanganKeluarga = 0.20 * GajiPokok
else: 
    TunjanganKeluarga = 0

GajiKotor = GajiPokok + TunjanganJabatan + TunjanganKeluarga
ZakatProfesi = (0, 0.025)[Agama == 'Kristen Protestan' and GajiKotor <= 6000000]
GajiBersih = GajiKotor - ZakatProfesi

print(
    '_ _ _ _ _ _ _ _ _ _ _ _'
    '\nSLIP GAJI PT. Renalmed'
    '\nNama Pegawai\t\t :', Pegawai,
    '\nAgama\t\t\t :', Agama, 
    '\nJumlah Anak\t\t :', Anak,
    '\nGaji Pokok\t\t :Rp.', GajiPokok,
    '\nTunjangan Jabatan\t :Rp.', TunjanganJabatan,
    '\nTunjangan Keluarga\t :Rp.', TunjanganKeluarga,
    '\nGaji Kotor\t\t :Rp.', GajiKotor,
    '\nZakat Profesi\t\t :Rp.', ZakatProfesi,
    '\nTake Home\t\t :Rp.', GajiBersih
)