[
  {
    $lookup: {
      from: "Montadoras",
      localField: "Montadora",
      foreignField: "Montadora",
      as: "montadora_info"
    }
  },
  {
    $unwind: "$montadora_info"
  },
  {
    $group: {
      _id: "$montadora_info.País",
      Carros: {
        $push: {
          carro: "$Carro",
          cor: "$Cor",
          Montadora: "$Montadora"
        }
      }
    }
  }
]
