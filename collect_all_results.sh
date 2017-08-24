
echo "running all python scripts"
echo "for directory: "$1

echo "check the mu map"
read input

mkdir -p "../results"

python make_dens_vs_ogm.py $1
python make_xsc_vs_ogm.py $1
python make_xcdw_vs_ogm.py $1

rm auto_checkpoint.txt
python make_auto_vs_ogm.py $1 X_avg
python make_auto_vs_ogm.py $1 X_avg complete

rm auto_checkpoint.txt
python make_auto_vs_ogm.py $1 X0
python make_auto_vs_ogm.py $1 X0 complete
