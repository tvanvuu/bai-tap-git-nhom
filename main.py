def tinh_thue_thu_nhap(thu_nhap):
  # Cập nhật công thức Thuế tại đây
  thu_nhap_tinh_thue = thu_nhap - 4000000
  return max (0, thu_nhap_tinh_thue * 0.05)

print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(10000000))
