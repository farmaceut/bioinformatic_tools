# Find .sdf molecules, optimize them with Open-Babel and convert to VINA-friendly .pdbqt format

find ~+ -name "*.sdf" |  while read line; do
  cd "$(dirname "${line}")";
  obminimize "$(basename "${line}")" > "$(basename "${line}" | cut -f 1 -d '.')"_opt.sdf;
  obabel $(basename ${line} | cut -f 1 -d '.')_opt.sdf -O $(basename ${line} | cut -f 1 -d '.')_opt.pdbqt;
done
