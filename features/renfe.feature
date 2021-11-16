Feature: Renfe

 Scenario: compra billete
   Given en el portal de renfe
   When selecciono origen madrid
   And selecciono destino barcelona
   Then selecciono un billete
   When