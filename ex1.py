class Movie :
    def __init__(self, movie_code, movie_name, production_cost, ticket_price, tickets_sold):
        self.movie_code      = movie_code      # Mã phim
        self.movie_name      = movie_name      # Tên phim
        self.production_cost = production_cost # Chi phí sản xuất
        self.ticket_price    = ticket_price    # Giá vé
        self.tickets_sold    = tickets_sold    # Số vé đã bán

        self.revenue = 0                       # Doanh thu
        self.profit  = 0                       # Lợi nhuận
        self.rating  = ""                      # Đánh giá

        self.calculate_revenue()
        self.calculate_profit()
        self.evaluate_rating()
    def calculate_revenue(self):
        revenue = self.ticket_price * self.tickets_sold
        self.revenue = revenue
    
    def calculate_profit(self):
        profit = self.revenue - self.production_cost
        self.profit = profit
    
    def evaluate_rating(self):
        if self.profit < 50000000 :
            self.rating = "Thất bại"
        elif self.profit < 200000000 :
            self.rating = "Trung bình"
        elif self.profit < 500000000 :
            self.rating = "Thành công"
        else:
            self.rating = "Bom tấn"
class MovieManager:
    def __init__(self):
        self.movies = []
    def find_code(self, code):
        for mov in self.movies:
            if mov.movie_code == code:
                return mov
        return None
    def add_movie(self):
        while True :
            add_code = input("Mời bạn nhập vào mã phim mới : ")
            if not add_code:
                print("Mã phim không được để trống")
                return
            if self.find_code(add_code):
                print("Mã phim đã tồn tại")
                return
            break
        while True :
            movie_name = input("Mời bạn Nhập vào tên phim :")
            if not movie_name:
                print("Tên phim không được để trống")
                return
            break
        while True :
            try:
                production_cost = input(int("mời bạn nhập vào chi phí sản xuất"))
                if production_cost < 0:
                    print("Chi phí sản xuất không được nhỏ hơn 0")
                    continue
                break
            except ValueError:
                print("dữ liệu không hợp lệ")
        while True :
            try:
                ticket_price = input(int("Mời bạn nhập vào giá vé"))
                if ticket_price < 0:
                    print("Giá vé không được nhỏ hơn 0")
                    continue
                break
            except ValueError:
                print("dữ liệu không hợp lệ")
        while True :
            try:
                tickets_sold = input(int("Mời bạn nhập vào số vé đá bán"))
                if tickets_sold < 0:
                    print("Số vé đá bán không được nhỏ hơn 0")
                    continue
                break
            except ValueError:
                print("dữ liệu không hợp lệ")


    def show_all_movies(self):
        if not self.movies:
            print("Danh sách phim đang rỗng ")
        else:
            print("==================================================================================================================")
            print(f"|{'Mã phim'}|{'Tên phim'}|{'Chi phí sản xuất'}|{'Giá vé'}|{'Số vé bán'}|{'Doanh thu'}|{'Lợi nhuận'}|{'Đánh giá'}|")
            print("==================================================================================================================")
            for m in self.movies:
                print(f"|{m.movie_code}|{m.movie_name }|{m.production_cost}|{m.ticket_price}|{m.tickets_sold }|{m.revenue }|{m.profit}|{m.rating }|")
            print("==================================================================================================================")

    def update_movie(self):
        pass
    def delete_movie(self):
        pass
    def search_movie(self):
        pass
def show_menu():
    print("""
            =============== MOVIE MANAGER ===============

            1. Hiển thị danh sách phim
            2. Thêm phim mới
            3. Cập nhật phim
            4. Xóa phim
            5. Tìm kiếm phim
            6. Thoát

            ============================================
            """)
def main():
    manager = MovieManager()
    while True:
        show_menu()
        choice = input("mời bạn nhập vào lựa chọn : ")
        match choice:
            case "1":
                manager.show_all_movies()
            case "2":
                manager.add_movie()
            case "3":
                manager.update_movie()
            case "4":
                manager.delete_movie()
            case "5":
                manager.search_movie()
            case "6":
                print("Thoát chương trình")
                break
            case _:
                print("lựa chọn không hợp lệ ")
