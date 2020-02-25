def readFasta(path):
  f = open(path,"r")
  test = []
  fasta = []
  for line in f:
    line = line.strip()
    if not line:
      continue
    if line.startswith(">"):
      active_sequence_name = line[1:]
      if active_sequence_name not in fasta:
        test.append(''.join(fasta))
        fasta = []
        continue
    sequence = line
    fasta.append(sequence)
  return(test)
