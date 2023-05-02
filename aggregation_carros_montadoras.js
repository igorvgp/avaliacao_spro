[
  {
    $lookup:
      {
        from: "Montadoras",
        localField: "Montadora",
        foreignField: "Montadora",
        as: "montadora_info",
      },
  },
  {
    $project: {
      _id: 0,
      Carro: 1,
      Cor: 1,
      Montadora: 1,
      Montadoras:"$montadora_info",
      pais: {$arrayElemAt:["$montadora_info.País",0]}
    },
  },

  
]
