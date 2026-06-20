class Movie:
    def __init__(self, movie_code, movie_name, production_cost, ticket_price, tickets_sold):
        self.movie_code = movie_code
        self.movie_name = movie_name
        self.production_cost = production_cost
        self.ticket_price = ticket_price
        self.tickets_sold = tickets_sold

        self.revenue = 0
        self.profit = 0
        self.rating = ""

        self.calculate_revenue()
        self.calculate_profit()
        self.evaluate_rating()

    def calculate_revenue(self):
        self.revenue = self.ticket_price * self.tickets_sold

    def calculate_profit(self):
        self.profit = self.revenue - self.production_cost

    def evaluate_rating(self):
        if self.profit < 50000000:
            self.rating = "Thất bại"
        elif self.profit < 200000000:
            self.rating = "Trung bình"
        elif self.profit < 500000000:
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
        while True:
            add_code = input("Mời bạn nhập vào mã phim mới : ")

            if not add_code:
                print("Mã phim không được để trống")
                continue

            if self.find_code(add_code):
                print("Mã phim đã tồn tại")
                continue

            break

        while True:
            movie_name = input("Mời bạn nhập vào tên phim : ")

            if not movie_name:
                print("Tên phim không được để trống")
                continue

            break

        while True:
            try:
                production_cost = float(input("Mời bạn nhập vào chi phí sản xuất : "))

                if production_cost < 0:
                    print("Chi phí sản xuất phải >= 0")
                    continue

                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        while True:
            try:
                ticket_price = float(input("Mời bạn nhập vào giá vé : "))

                if ticket_price < 0:
                    print("Giá vé phải >= 0")
                    continue

                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        while True:
            try:
                tickets_sold = int(input("Mời bạn nhập vào số vé đã bán : "))

                if tickets_sold < 0:
                    print("Số vé đã bán phải >= 0")
                    continue

                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        new_movie = Movie(
            add_code,
            movie_name,
            production_cost,
            ticket_price,
            tickets_sold
        )

        self.movies.append(new_movie)

        print("Thêm phim thành công !")

    def show_all_movies(self):
        if not self.movies:
            print("Danh sách phim đang rỗng ")
            return

        print("======================================================================================================")
        print("|Mã phim|Tên phim|Chi phí sản xuất|Giá vé|Số vé bán|Doanh thu|Lợi nhuận|Đánh giá|")
        print("======================================================================================================")

        for m in self.movies:
            print(
                f"|{m.movie_code}|{m.movie_name}|{m.production_cost}|"
                f"{m.ticket_price}|{m.tickets_sold}|{m.revenue}|"
                f"{m.profit}|{m.rating}|"
            )

        print("======================================================================================================")

    def update_movie(self):
        while True:
            update_code = input("Mời bạn nhập vào mã phim cần cập nhật : ")

            if not update_code:
                print("Mã phim không được để trống")
                continue

            movie = self.find_code(update_code)

            if not movie:
                print("Mã phim không tồn tại")
                continue

            break

        while True:
            movie_name = input("Mời bạn nhập vào tên phim mới : ")

            if not movie_name:
                print("Tên phim không được để trống")
                continue

            break

        while True:
            try:
                production_cost = float(input("Mời bạn nhập vào chi phí sản xuất mới : "))

                if production_cost < 0:
                    print("Chi phí sản xuất phải >= 0")
                    continue

                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        while True:
            try:
                ticket_price = float(input("Mời bạn nhập vào giá vé mới : "))

                if ticket_price < 0:
                    print("Giá vé phải >= 0")
                    continue

                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        while True:
            try:
                tickets_sold = int(input("Mời bạn nhập vào số vé đã bán mới : "))

                if tickets_sold < 0:
                    print("Số vé đã bán phải >= 0")
                    continue

                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        movie.movie_name = movie_name
        movie.production_cost = production_cost
        movie.ticket_price = ticket_price
        movie.tickets_sold = tickets_sold

        movie.calculate_revenue()
        movie.calculate_profit()
        movie.evaluate_rating()

        print("Cập nhật phim thành công !")

    def delete_movie(self):
        while True:
            delete_code = input("Mời bạn nhập vào mã phim cần xóa : ")

            if not delete_code:
                print("Mã phim không được để trống")
                continue

            movie = self.find_code(delete_code)

            if not movie:
                print("Mã phim không tồn tại")
                continue

            break

        self.movies.remove(movie)

        print("Xóa phim thành công !")

    def search_movie(self):
        keyword = input("Mời bạn nhập vào mã phim hoặc tên phim : ").lower()

        found = False

        for movie in self.movies:
            if keyword in movie.movie_code.lower() or keyword in movie.movie_name.lower():
                found = True

                print("====================================")
                print(f"Mã phim : {movie.movie_code}")
                print(f"Tên phim : {movie.movie_name}")
                print(f"Chi phí sản xuất : {movie.production_cost}")
                print(f"Giá vé : {movie.ticket_price}")
                print(f"Số vé bán : {movie.tickets_sold}")
                print(f"Doanh thu : {movie.revenue}")
                print(f"Lợi nhuận : {movie.profit}")
                print(f"Đánh giá : {movie.rating}")
                print("====================================")

        if not found:
            print("Không tìm thấy phim")


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

        choice = input("Mời bạn nhập vào lựa chọn : ")

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
                print("Lựa chọn không hợp lệ")

    lmain()
