##1
# class Transport:
#     def __init__(self, model: str, yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"
#
#
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, Yonilg'i: {self.yonilgi_turi}"
#
#
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
#
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())

## 2
# class kitob:
#     def __init__(self, nom: str, mualifi: str, yil: int) -> None:
#         self.nom = nom
#         self.mualifi = mualifi
#         self.yil = yil
#
#
#     def taqdimot(self) -> str:
#         return "\"{nom}\" - {mualifi} ({yil})"
#
# class ElektronKitob(Kitob):
#     def __init__(self, nom: str, mualifi: str, yil: int, fayl_hajmi_mb: str) -> None:
#         super().__init__(mualifi, nom, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self) -> str:
#         baza = super().taqdimot()
#         return f" [Elektron, {fayl_hajmi_mb}MB]"
#
#
# class AudioKitob(Kitob):
#     def __init__(self, nom: str, mualifi: str, yil: int, davomiylik_soat: str) -> None:
#         super().__init__(mualifi, nom, yil)
#         self.davomiylik_soat = davomiylik_soat
#
#     def taqdimot(self) -> str:
#         baza = super().taqdimot()
#         return f" [Elektron, {davomiylik_soat}MB]"
#
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
#
# print(e.taqdimot())
# print(a.taqdimot())

## 3
# class Xodim:
#     def __init__(self, ism, asosiy_maosh ):
#         self.ims = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self):
#         return f"asosiy_maosh {self.asosiy_maosh}"
#
#     def malumot(self) :
#         return f"Ism: {ism}, Oylik: {oylik()}"
#
# class Oqsoch(Xodim):
#     def __init__(self, ism, asosiy_maosh, bonus_foiz):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
#
#     def oylik(self) -> str:
#         baza = super().oylik()
#         return f"{baza}, bonus_foiz: {self.bonus_foiz}"
#
#
# class SoatbayXodim(Xodim):
#     def __init__(self,ism, asosiy_maosh ,soat, soatlik_stavka ):
#         super().__init__(ism,asosiy_maosh, soat)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
#
#
#
#
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
#
# print(o.malumot())
# print(s.malumot())
