import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime, timedelta
import random
import string
import json

# ==================================================
# GLOBAL THEME
# ==================================================
BG = "#f4f6f9"
PRIMARY = "#0d6efd"
SUCCESS = "#198754"
DANGER = "#dc3545"
WARNING = "#ffc107"
DARK = "#212529"
WHITE = "#ffffff"
LIGHT_GRAY = "#e9ecef"
INFO = "#17a2b8"

# ==================================================
# COMPREHENSIVE INDIAN RAILWAY DATA
# ==================================================

# Mumbai Local - Western Line
WESTERN_LINE = [
    "Churchgate", "Marine Lines", "Charni Road", "Grant Road", 
    "Mumbai Central", "Mahalaxmi", "Lower Parel", "Prabhadevi",
    "Dadar", "Matunga Road", "Mahim", "Bandra", "Khar Road",
    "Santacruz", "Vile Parle", "Andheri", "Jogeshwari", "Ram Mandir",
    "Goregaon", "Malad", "Kandivali", "Borivali", "Dahisar",
    "Mira Road", "Bhayandar", "Naigaon", "Vasai Road", "Nalla Sopara",
    "Virar"
]

# Mumbai Local - Central Line
CENTRAL_LINE = [
    "CSMT", "Masjid", "Sandhurst Road", "Byculla", "Chinchpokli",
    "Currey Road", "Parel", "Dadar", "Matunga", "Sion", "Kurla",
    "Vidyavihar", "Ghatkopar", "Vikhroli", "Kanjurmarg", "Bhandup",
    "Nahur", "Mulund", "Thane", "Kalwa", "Mumbra", "Diva",
    "Kopar", "Dombivli", "Thakurli", "Kalyan", "Shahad", "Ambivli",
    "Titwala", "Khadavli", "Vasind", "Asangaon", "Atgaon", "Khardi",
    "Kasara"
]

# Mumbai Local - Harbour Line
HARBOUR_LINE = [
    "CSMT", "Masjid", "Sandhurst Road", "Dockyard Road", "Reay Road",
    "Cotton Green", "Sewri", "Wadala Road", "King's Circle", "Mahim",
    "Bandra", "Khar Road", "Santacruz", "Vile Parle", "Andheri",
    "Kurla", "Tilak Nagar", "Chembur", "Govandi", "Mankhurd",
    "Vashi", "Sanpada", "Juinagar", "Nerul", "Seawoods",
    "Belapur CBD", "Kharghar", "Mansarovar", "Khandeshwar", "Panvel"
]

# Trans-Harbour Line
TRANS_HARBOUR = [
    "Thane", "Airoli", "Rabale", "Ghansoli", "Kopar Khairane",
    "Turbhe", "Sanpada", "Juinagar", "Nerul", "Seawoods",
    "Belapur CBD", "Kharghar", "Mansarovar", "Khandeshwar", "Panvel"
]

# Major Cities - North India
NORTH_STATIONS = [
    "New Delhi", "Old Delhi", "Hazrat Nizamuddin", "Anand Vihar",
    "Delhi Cantt", "Delhi Sarai Rohilla",
    "Chandigarh", "Amritsar", "Jammu Tawi", "Pathankot",
    "Ludhiana", "Jalandhar", "Ambala", "Karnal", "Panipat",
    "Agra Cantt", "Mathura Jn", "Bharatpur", "Gwalior",
    "Jhansi", "Kanpur Central", "Lucknow", "Varanasi Jn",
    "Allahabad Jn", "Gorakhpur", "Bareilly", "Moradabad"
]

# Major Cities - South India
SOUTH_STATIONS = [
    "Chennai Central", "Chennai Egmore", "Tambaram", "Chengalpattu",
    "Bengaluru City", "Bengaluru Cantonment", "Yesvantpur Jn",
    "Mysuru Jn", "Hubballi Jn",
    "Hyderabad Deccan", "Secunderabad Jn", "Kacheguda",
    "Vijayawada Jn", "Visakhapatnam", "Rajahmundry",
    "Thiruvananthapuram Central", "Ernakulam Jn", "Kochi",
    "Kozhikode", "Thrissur", "Kannur",
    "Coimbatore Jn", "Madurai Jn", "Tiruchchirappalli Jn",
    "Salem Jn", "Tirupati"
]

# Major Cities - East India
EAST_STATIONS = [
    "Howrah Jn", "Sealdah", "Kolkata", "Kharagpur Jn",
    "Bhubaneswar", "Puri", "Cuttack",
    "Patna Jn", "Gaya Jn", "Danapur", "Muzaffarpur Jn",
    "Ranchi", "Dhanbad Jn", "Tatanagar Jn", "Asansol Jn",
    "Malda Town", "New Jalpaiguri", "Siliguri Jn",
    "Guwahati", "Dibrugarh", "Kamakhya Jn"
]

# Major Cities - West India
WEST_STATIONS = [
    "Mumbai CST", "Mumbai Central", "Lokmanya Tilak", "Dadar",
    "Thane", "Kalyan Jn", "Panvel",
    "Pune Jn", "Lonavala", "Satara",
    "Ahmedabad Jn", "Surat", "Vadodara Jn", "Rajkot Jn",
    "Bhavnagar", "Jamnagar",
    "Nagpur Jn", "Wardha Jn",
    "Indore Jn", "Bhopal Jn", "Jabalpur", "Ujjain Jn",
    "Ratlam Jn",
    "Jaipur Jn", "Ajmer Jn", "Jodhpur Jn", "Udaipur City",
    "Bikaner Jn", "Kota Jn"
]

# Railway Zones
ZONES = {
    "Mumbai Local": {
        "Western Line": WESTERN_LINE,
        "Central Line": CENTRAL_LINE,
        "Harbour Line": HARBOUR_LINE,
        "Trans-Harbour": TRANS_HARBOUR
    },
    "North Zone": NORTH_STATIONS,
    "South Zone": SOUTH_STATIONS,
    "East Zone": EAST_STATIONS,
    "West Zone": WEST_STATIONS
}

# Travel Classes with realistic pricing
CLASSES = [
    "Second Sitting (2S)",
    "Sleeper Class (SL)", 
    "AC 3 Tier (3A)",
    "AC 2 Tier (2A)",
    "First Class AC (1A)",
    "AC Chair Car (CC)",
    "First Class (FC)"
]

# Journey Types
JOURNEY_TYPES = ["Single Journey", "Return Journey"]

# Base fare structure (per km)
BASE_FARES = {
    "Second Sitting (2S)": 0.5,
    "Sleeper Class (SL)": 1.0,
    "AC 3 Tier (3A)": 2.5,
    "AC 2 Tier (2A)": 3.5,
    "First Class AC (1A)": 5.0,
    "AC Chair Car (CC)": 2.0,
    "First Class (FC)": 3.0
}

# Distance matrix (simplified - in real app, use actual distances)
# For demo, we calculate based on index difference
DISTANCE_MULTIPLIER = {
    "local": 5,      # 5 km between local stations
    "regional": 50,  # 50 km between regional stations
    "long": 100      # 100 km base for long distance
}

# ==================================================
# APP STATE
# ==================================================
class State:
    def __init__(self):
        self.phone = None
        self.wallet = 1000  # Higher initial balance for long-distance
        self.tickets = []
        self.transaction_history = []
        self.user_name = None
        self.email = None

state = State()

# ==================================================
# UTILITIES
# ==================================================
def generate_otp():
    return str(random.randint(100000, 999999))

def gen_pnr():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def gen_txn_id():
    return 'TXN' + ''.join(random.choices(string.digits, k=12))

def get_all_stations():
    """Get all stations from all zones"""
    all_stations = []
    
    # Mumbai Local
    for line_name, stations in ZONES["Mumbai Local"].items():
        all_stations.extend(stations)
    
    # Other zones
    all_stations.extend(ZONES["North Zone"])
    all_stations.extend(ZONES["South Zone"])
    all_stations.extend(ZONES["East Zone"])
    all_stations.extend(ZONES["West Zone"])
    
    # Remove duplicates and sort
    return sorted(list(set(all_stations)))

def find_station_zone(station):
    """Find which zone/line a station belongs to"""
    # Check Mumbai Local
    for line_name, stations in ZONES["Mumbai Local"].items():
        if station in stations:
            return ("Mumbai Local", line_name)
    
    # Check other zones
    for zone_name in ["North Zone", "South Zone", "East Zone", "West Zone"]:
        if station in ZONES[zone_name]:
            return (zone_name, None)
    
    return (None, None)

def calculate_distance(src, dest):
    """Calculate approximate distance between stations"""
    src_zone, src_line = find_station_zone(src)
    dest_zone, dest_line = find_station_zone(dest)
    
    # Same Mumbai local line
    if src_zone == "Mumbai Local" and dest_zone == "Mumbai Local" and src_line == dest_line:
        line_stations = ZONES["Mumbai Local"][src_line]
        src_idx = line_stations.index(src)
        dest_idx = line_stations.index(dest)
        return abs(dest_idx - src_idx) * DISTANCE_MULTIPLIER["local"]
    
    # Different Mumbai local lines (transfer required)
    elif src_zone == "Mumbai Local" and dest_zone == "Mumbai Local":
        return 30 + (random.randint(5, 15) * DISTANCE_MULTIPLIER["local"])
    
    # Regional within same zone
    elif src_zone == dest_zone and src_zone != "Mumbai Local":
        zone_stations = ZONES[src_zone]
        if src in zone_stations and dest in zone_stations:
            src_idx = zone_stations.index(src)
            dest_idx = zone_stations.index(dest)
            return abs(dest_idx - src_idx) * DISTANCE_MULTIPLIER["regional"]
        return DISTANCE_MULTIPLIER["regional"] * 5
    
    # Long distance (different zones)
    else:
        # Simplified: random long distance
        return random.randint(500, 3000)

def calc_fare(src, dest, travel_class, journey_type, qty):
    """Calculate ticket fare"""
    if src == dest:
        return 0
    
    distance = calculate_distance(src, dest)
    base_rate = BASE_FARES[travel_class]
    base_fare = distance * base_rate
    
    # Minimum fare
    base_fare = max(base_fare, 10)
    
    # Apply quantity
    total = base_fare * qty
    
    # Return journey discount (10% off on return)
    if journey_type == "Return Journey":
        total = total * 2 * 0.95
    
    return round(total, 2)

def get_validity(journey_type, distance):
    """Get ticket validity based on journey type and distance"""
    if distance <= 100:  # Local/short distance
        return datetime.now() + (timedelta(hours=3) if journey_type == "Single Journey" else timedelta(hours=48))
    else:  # Long distance
        return datetime.now() + timedelta(days=1 if journey_type == "Single Journey" else 7)
def get_route_path(src, dest):
    src_zone, src_line = find_station_zone(src)
    dest_zone, dest_line = find_station_zone(dest)

    # Same Mumbai local line
    if src_zone == "Mumbai Local" and dest_zone == "Mumbai Local" and src_line == dest_line:
        stations = ZONES["Mumbai Local"][src_line]
        i, j = stations.index(src), stations.index(dest)
        return stations[i:j+1] if i < j else stations[j:i+1][::-1]

    # Same non-local zone
    if src_zone == dest_zone and src_zone != "Mumbai Local":
        stations = ZONES[src_zone]
        i, j = stations.index(src), stations.index(dest)
        return stations[i:j+1] if i < j else stations[j:i+1][::-1]

    # Different zones (long-distance simplified)
    return [src, "— INTER ZONE TRAVEL —", dest]


# ==================================================
# AI ASSISTANT (ENHANCED)
# ==================================================
def ai_reply(q):
    q = q.lower()
    
    if "station" in q and ("mumbai" in q or "local" in q):
        return f"Mumbai Local has {len(WESTERN_LINE)} Western Line stations, {len(CENTRAL_LINE)} Central Line stations, and {len(HARBOUR_LINE)} Harbour Line stations."
    
    if "zone" in q or "how many" in q:
        return f"We serve {len(get_all_stations())} stations across India including Mumbai Local (Western, Central, Harbour, Trans-Harbour), North, South, East, and West zones."
    
    if "cheap" in q or "cheapest" in q:
        return "Second Sitting (2S) is the cheapest class at ₹0.50/km. For comfort, try Sleeper Class at ₹1/km."
    
    if "expensive" in q or "premium" in q:
        return "First Class AC (1A) is the most premium at ₹5/km with best amenities."
    
    if "ac" in q and "class" in q:
        return "AC classes: 3A (₹2.5/km), 2A (₹3.5/km), 1A (₹5/km), CC (₹2/km). All have air conditioning and reserved seats."
    
    if "return" in q:
        return "Return journeys get 5% discount and are valid for 48 hours (local) or 7 days (long distance)."
    
    if "valid" in q or "expire" in q:
        return "Local tickets: 3 hours (single) or 48 hours (return). Long distance: 1 day (single) or 7 days (return)."
    
    if "wallet" in q or "balance" in q:
        return f"Your wallet balance is ₹{state.wallet:.2f}"
    
    if "book" in q or "how to" in q:
        return "To book: Select zone/line → Choose source & destination → Select class → Choose passengers → Pay & book!"
    
    if "western" in q:
        return f"Western Line has {len(WESTERN_LINE)} stations from Churchgate to Virar."
    
    if "central" in q:
        return f"Central Line has {len(CENTRAL_LINE)} stations from CSMT to Kasara."
    
    if "harbour" in q:
        return f"Harbour Line has {len(HARBOUR_LINE)} stations from CSMT to Panvel."
    
    if "help" in q:
        return "Ask me about: stations, fares, classes, booking process, zones, or specific routes!"
    
    return "I can help with stations, fares, booking, and route information. Try: 'Show me Western line stations' or 'What's the cheapest class?'"

# ==================================================
# OTP WINDOW
# ==================================================
def otp_window(parent, otp):
    win = tk.Toplevel(parent)
    win.geometry("350x250")
    win.configure(bg=WHITE)
    win.title("OTP Verification")
    win.resizable(False, False)
    win.transient(parent)
    win.grab_set()

    tk.Label(win, text="Enter OTP",
             font=("Arial", 16, "bold"),
             bg=WHITE, fg=DARK).pack(pady=20)

    entry = tk.Entry(win, font=("Arial", 18), justify="center", width=10)
    entry.pack(pady=10)
    entry.focus_set()

    verified = {"ok": False}

    def check():
        if entry.get() == otp:
            verified["ok"] = True
            win.destroy()
        else:
            messagebox.showerror("Error", "Invalid OTP", parent=win)
            entry.delete(0, tk.END)

    def on_enter(event):
        check()

    entry.bind('<Return>', on_enter)

    tk.Button(win, text="Verify OTP",
              bg=SUCCESS, fg=WHITE,
              font=("Arial", 12, "bold"),
              padx=20, pady=10,
              command=check).pack(pady=15)

    parent.wait_window(win)
    return verified["ok"]

# ==================================================
# LOGIN PAGE
# ==================================================
class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Indian Railways - RailEase")
        self.geometry("500x550")
        self.configure(bg=BG)
        self.resizable(False, False)

        # Header
        header = tk.Frame(self, bg=PRIMARY, height=120)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🚂 RailEase ",
                 font=("Arial", 26, "bold"),
                 fg=WHITE, bg=PRIMARY).pack(pady=15)
        
        tk.Label(header, text="Book Tickets Across India",
                 font=("Arial", 12),
                 fg=WHITE, bg=PRIMARY).pack()

        # Content
        content = tk.Frame(self, bg=BG)
        content.pack(fill="both", expand=True, padx=40, pady=30)

        tk.Label(content, text="Welcome to Indian Railways",
                 font=("Arial", 18, "bold"),
                 bg=BG, fg=DARK).pack(pady=10)

        tk.Label(content, text="Enter Mobile Number",
                 font=("Arial", 12),
                 bg=BG, fg=DARK).pack(pady=10)

        self.phone = tk.Entry(content, font=("Arial", 14), justify="center", width=15)
        self.phone.pack(pady=10)
        self.phone.focus_set()

        tk.Button(content, text="Send OTP",
                  bg=PRIMARY, fg=WHITE,
                  font=("Arial", 12, "bold"),
                  width=20, height=2,
                  command=self.send_otp).pack(pady=20)

        # Info
        info_frame = tk.Frame(content, bg=LIGHT_GRAY, relief="solid", bd=1)
        info_frame.pack(fill="x", pady=10)
        
        tk.Label(info_frame, text="Coverage:",
                 font=("Arial", 10, "bold"),
                 bg=LIGHT_GRAY).pack(pady=(10, 5))
        
        tk.Label(info_frame, 
                 text="Mumbai Local (Western, Central, Harbour)\nMajor Cities Across India",
                 font=("Arial", 9),
                 bg=LIGHT_GRAY, fg=DARK).pack(pady=(0, 10))

    def send_otp(self):
        number = self.phone.get().strip()
        
        if not number:
            return messagebox.showerror("Error", "Please enter mobile number")
        
        if not number.isdigit() or len(number) != 10:
            return messagebox.showerror("Error", "Enter valid 10-digit mobile number")

        otp = generate_otp()
        messagebox.showinfo("OTP Sent", f"Your OTP is: {otp}")

        if otp_window(self, otp):
            state.phone = number
            self.destroy()
            App().mainloop()
try:
    if not hasattr(state, 'user_name'):
        state.user_name = None
    if not hasattr(state, 'season_pass'):
        state.season_pass = None
except Exception:
    pass

def validate_aadhaar(a):
    return isinstance(a, str) and a.isdigit() and len(a) == 12

# Optional Season Pass Page (won't break if navbar not wired)
class SeasonPass(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG)
        self.controller = controller
        frame = tk.Frame(self, bg=BG)
        frame.pack(fill="both", expand=True, padx=40, pady=30)
        tk.Label(frame, text="Mumbai Local Season Pass",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(pady=20)
        box = tk.Frame(frame, bg=WHITE, bd=1, relief="solid")
        box.pack(padx=20, pady=20)
        tk.Label(box, text="Aadhaar Number (Demo)", bg=WHITE).pack(pady=10)
        self.aadhaar = tk.Entry(box, font=("Arial", 12), width=25)
        self.aadhaar.pack(pady=5)
        tk.Button(box, text="Verify & Activate Pass",
                  bg=SUCCESS, fg=WHITE,
                  font=("Arial", 12),
                  command=self.activate).pack(pady=20)

    def activate(self):
        if not validate_aadhaar(self.aadhaar.get()):
            return messagebox.showerror("Error", "Invalid Aadhaar Number")
        from datetime import datetime, timedelta
        state.season_pass = datetime.now() + timedelta(days=30)
        messagebox.showinfo("Success", "Season Pass Active for 30 Days")


# ==================================================
# MAIN APP
# ==================================================
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Indian Railways - RailEase")
        self.geometry("1200x750")
        self.configure(bg=BG)
        self.minsize(1000, 650)

        # NAVBAR
        nav = tk.Frame(self, bg=DARK, height=65)
        nav.pack(fill="x")
        nav.pack_propagate(False)

        tk.Label(nav, text="🚂 Indian Railways",
                 font=("Arial", 18, "bold"),
                 fg=WHITE, bg=DARK).pack(side="left", padx=20)

        self.nav_buttons = {}
        for name, page in [
            ("🏠 Home", "Home"),
            ("🎫 Book Ticket", "Book"),
            ("📋 My Tickets", "Tickets"),
            ("💳 Wallet", "Wallet"),
            ("🗺️ Route Map", "Routes"),
            ("🤖 AI Help", "AI")
        ]:
            btn = tk.Button(nav, text=name,
                          bg=DARK, fg=WHITE,
                          font=("Arial", 10),
                          relief="flat",
                          activebackground=PRIMARY,
                          command=lambda p=page: self.show(p))
            btn.pack(side="left", padx=6)
            self.nav_buttons[page] = btn

        tk.Label(nav, text=f"📱 {state.phone}",
                 font=("Arial", 9),
                 fg=WHITE, bg=DARK).pack(side="right", padx=20)

        # CONTAINER
        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for P in (Home, Book, Tickets, Wallet, Routes, AI):
            frame = P(self.container, self)
            self.pages[P.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show("Home")

    def show(self, page):
        frame = self.pages[page]
        if hasattr(frame, 'refresh'):
            frame.refresh()
        frame.tkraise()
        
        for p, btn in self.nav_buttons.items():
            if p == page:
                btn.config(bg=PRIMARY)
            else:
                btn.config(bg=DARK)

# ==================================================
# PAGES
# ==================================================
class Home(tk.Frame):
    def __init__(self, p, c):
        super().__init__(p, bg=BG)
        self.controller = c
        
        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=40, pady=30)
        
        tk.Label(main, text="Welcome to Indian Railways Booking!",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(pady=20)
        
        self.info = tk.Label(main, font=("Arial", 12), bg=BG, fg=DARK)
        self.info.pack(pady=10)
        
        # Stats
        stats = tk.Frame(main, bg=BG)
        stats.pack(fill="x", pady=20)
        
        self.wallet_card = self.make_card(stats, "💰 Wallet Balance", "₹0")
        self.wallet_card.pack(side="left", padx=10, fill="both", expand=True)
        
        self.ticket_card = self.make_card(stats, "🎫 Tickets Booked", "0")
        self.ticket_card.pack(side="left", padx=10, fill="both", expand=True)
        
        self.station_card = self.make_card(stats, "🚉 Stations Available", str(len(get_all_stations())))
        self.station_card.pack(side="left", padx=10, fill="both", expand=True)
        
        # Coverage info
        coverage = tk.Frame(main, bg=WHITE, relief="solid", bd=1)
        coverage.pack(fill="x", pady=20)
        
        tk.Label(coverage, text="🗺️ Network Coverage",
                 font=("Arial", 14, "bold"),
                 bg=WHITE, fg=DARK).pack(pady=10)
        
        coverage_text = f"""
        Mumbai Local: Western ({len(WESTERN_LINE)}), Central ({len(CENTRAL_LINE)}), 
        Harbour ({len(HARBOUR_LINE)}), Trans-Harbour ({len(TRANS_HARBOUR)})
        
        North Zone: {len(NORTH_STATIONS)} major stations
        South Zone: {len(SOUTH_STATIONS)} major stations
        East Zone: {len(EAST_STATIONS)} major stations
        West Zone: {len(WEST_STATIONS)} major stations
        
        Total: {len(get_all_stations())} stations across India
        """
        
        tk.Label(coverage, text=coverage_text,
                 font=("Arial", 10),
                 bg=WHITE, fg=DARK,
                 justify="left").pack(pady=10, padx=20)
        
        # Quick actions
        actions = tk.Frame(main, bg=BG)
        actions.pack(pady=20)
        
        tk.Button(actions, text="📱 Book Ticket Now",
                  bg=PRIMARY, fg=WHITE,
                  font=("Arial", 13, "bold"),
                  padx=25, pady=12,
                  command=lambda: c.show("Book")).pack(side="left", padx=10)
        
        tk.Button(actions, text="🗺️ View Route Map",
                  bg=INFO, fg=WHITE,
                  font=("Arial", 13, "bold"),
                  padx=25, pady=12,
                  command=lambda: c.show("Routes")).pack(side="left", padx=10)

    def make_card(self, parent, title, value):
        card = tk.Frame(parent, bg=WHITE, relief="solid", bd=1)
        tk.Label(card, text=title, font=("Arial", 11), bg=WHITE, fg="gray").pack(pady=10)
        lbl = tk.Label(card, text=value, font=("Arial", 20, "bold"), bg=WHITE, fg=PRIMARY)
        lbl.pack(pady=10)
        card.value_label = lbl
        return card

    def refresh(self):
        self.info.config(text=f"Phone: {state.phone} | Wallet: ₹{state.wallet:.2f} | Tickets: {len(state.tickets)}")
        self.wallet_card.value_label.config(text=f"₹{state.wallet:.2f}")
        self.ticket_card.value_label.config(text=str(len(state.tickets)))

class Book(tk.Frame):
    def __init__(self, p, c):
        super().__init__(p, bg=BG)
        self.controller = c
        
        # Create scrollable frame
        canvas = tk.Canvas(self, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable = tk.Frame(canvas, bg=BG)
        
        self.scrollable.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main content
        main = tk.Frame(self.scrollable, bg=BG)
        main.pack(fill="both", expand=True, padx=40, pady=30)
        
        tk.Label(main, text="🎫 Book Your Railway Ticket",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(pady=20)
        
        form = tk.Frame(main, bg=WHITE, relief="solid", bd=1)
        form.pack(fill="both", expand=True, padx=20)
        
        fields = tk.Frame(form, bg=WHITE)
        fields.pack(pady=30, padx=40)
        
        # Zone/Line Selection
        tk.Label(fields, text="Select Route Type", font=("Arial", 12, "bold"), bg=WHITE).grid(row=0, column=0, sticky="w", pady=10, padx=10)
        self.route_type = ttk.Combobox(fields, 
                                       values=["All India (Select Any Station)", 
                                              "Mumbai Local - Western Line",
                                              "Mumbai Local - Central Line", 
                                              "Mumbai Local - Harbour Line",
                                              "Mumbai Local - Trans-Harbour"],
                                       state="readonly", font=("Arial", 10), width=30)
        self.route_type.grid(row=0, column=1, pady=10, padx=10)
        self.route_type.current(0)
        self.route_type.bind('<<ComboboxSelected>>', self.update_stations)
        
        # Source
        tk.Label(fields, text="🚉 From (Source)", font=("Arial", 11, "bold"), bg=WHITE).grid(row=1, column=0, sticky="w", pady=10, padx=10)
        self.src = ttk.Combobox(fields, values=get_all_stations(), state="readonly", font=("Arial", 10), width=30)
        self.src.grid(row=1, column=1, pady=10, padx=10)
        self.src.bind('<<ComboboxSelected>>', self.update_fare)
        
        # Destination
        tk.Label(fields, text="🎯 To (Destination)", font=("Arial", 11, "bold"), bg=WHITE).grid(row=2, column=0, sticky="w", pady=10, padx=10)
        self.dest = ttk.Combobox(fields, values=get_all_stations(), state="readonly", font=("Arial", 10), width=30)
        self.dest.grid(row=2, column=1, pady=10, padx=10)
        self.dest.bind('<<ComboboxSelected>>', self.update_fare)
        
        # Class
        tk.Label(fields, text="🚂 Travel Class", font=("Arial", 11, "bold"), bg=WHITE).grid(row=3, column=0, sticky="w", pady=10, padx=10)
        self.cls = ttk.Combobox(fields, values=CLASSES, state="readonly", font=("Arial", 10), width=30)
        self.cls.grid(row=3, column=1, pady=10, padx=10)
        self.cls.current(0)
        self.cls.bind('<<ComboboxSelected>>', self.update_fare)
        
        # Journey Type
        tk.Label(fields, text="↔️ Journey Type", font=("Arial", 11, "bold"), bg=WHITE).grid(row=4, column=0, sticky="w", pady=10, padx=10)
        self.jt = ttk.Combobox(fields, values=JOURNEY_TYPES, state="readonly", font=("Arial", 10), width=30)
        self.jt.grid(row=4, column=1, pady=10, padx=10)
        self.jt.current(0)
        self.jt.bind('<<ComboboxSelected>>', self.update_fare)
        
        # Passengers
        tk.Label(fields, text="👥 Passengers (1-6)", font=("Arial", 11, "bold"), bg=WHITE).grid(row=5, column=0, sticky="w", pady=10, padx=10)
        self.qty = tk.Spinbox(fields, from_=1, to=6, font=("Arial", 10), width=29)
        self.qty.grid(row=5, column=1, pady=10, padx=10)
        self.qty.bind('<KeyRelease>', self.update_fare)
        self.qty.bind('<<Increment>>', self.update_fare)
        self.qty.bind('<<Decrement>>', self.update_fare)
        
        # Fare preview
        self.fare_frame = tk.Frame(form, bg=LIGHT_GRAY, relief="solid", bd=1)
        self.fare_frame.pack(pady=15, fill="x", padx=20)
        
        self.fare_lbl = tk.Label(self.fare_frame, text="Select journey details to see fare", 
                                font=("Arial", 13), bg=LIGHT_GRAY, fg=DARK)
        self.fare_lbl.pack(pady=15)
        
        self.distance_lbl = tk.Label(self.fare_frame, text="", 
                                     font=("Arial", 10), bg=LIGHT_GRAY, fg="gray")
        self.distance_lbl.pack(pady=(0, 10))
        
        # Buttons
        btns = tk.Frame(form, bg=WHITE)
        btns.pack(pady=25)
        
        tk.Button(btns, text="💳 Pay & Book Ticket",
                  bg=SUCCESS, fg=WHITE,
                  font=("Arial", 13, "bold"),
                  padx=30, pady=15,
                  command=self.book).pack(side="left", padx=10)
        
        tk.Button(btns, text="🔄 Reset Form",
                  bg=DANGER, fg=WHITE,
                  font=("Arial", 13, "bold"),
                  padx=30, pady=15,
                  command=self.reset).pack(side="left", padx=10)

    def update_stations(self, event=None):
        """Update station list based on route type"""
        route = self.route_type.get()
        
        if route == "All India (Select Any Station)":
            stations = get_all_stations()
        elif "Western Line" in route:
            stations = WESTERN_LINE
        elif "Central Line" in route:
            stations = CENTRAL_LINE
        elif "Harbour Line" in route:
            stations = HARBOUR_LINE
        elif "Trans-Harbour" in route:
            stations = TRANS_HARBOUR
        else:
            stations = get_all_stations()
        
        self.src['values'] = stations
        self.dest['values'] = stations
        self.src.set('')
        self.dest.set('')
        self.update_fare()

    def update_fare(self, event=None):
        try:
            src = self.src.get()
            dest = self.dest.get()
            cls = self.cls.get()
            jt = self.jt.get()
            qty_str = self.qty.get()
            
            if not qty_str or not qty_str.isdigit():
                qty = 1
            else:
                qty = int(qty_str)
            
            if src and dest and cls and jt:
                if src == dest:
                    self.fare_lbl.config(text="⚠️ Source and destination cannot be same!", fg=DANGER)
                    self.distance_lbl.config(text="")
                    return
                
                fare = calc_fare(src, dest, cls, jt, qty)
                distance = calculate_distance(src, dest)
                
                if fare == 0:
                    self.fare_lbl.config(text="Invalid selection", fg=DANGER)
                    self.distance_lbl.config(text="")
                else:
                    self.fare_lbl.config(text=f"💰 Total Fare: ₹{fare:.2f}", fg=SUCCESS)
                    self.distance_lbl.config(text=f"📏 Distance: ~{distance} km | Passengers: {qty}")
            else:
                self.fare_lbl.config(text="Select all fields to see fare", fg=DARK)
                self.distance_lbl.config(text="")
        except Exception as e:
            self.fare_lbl.config(text="Enter valid details", fg=DANGER)
            self.distance_lbl.config(text="")

    def reset(self):
        self.route_type.current(0)
        self.update_stations()
        self.cls.current(0)
        self.jt.current(0)
        self.qty.delete(0, tk.END)
        self.qty.insert(0, "1")
        self.fare_lbl.config(text="Select journey details to see fare", fg=DARK)
        self.distance_lbl.config(text="")

    def refresh(self):
        pass

    def book(self):
        try:
            src = self.src.get()
            dest = self.dest.get()
            cls = self.cls.get()
            jt = self.jt.get()
            qty_str = self.qty.get()
            
            if not src or not dest or not cls or not jt:
                return messagebox.showerror("Error", "Please fill all fields")
            
            if not qty_str.isdigit():
                return messagebox.showerror("Error", "Enter valid passenger count")
            
            qty = int(qty_str)
            
            if qty < 1 or qty > 6:
                return messagebox.showerror("Error", "Passengers must be between 1-6")
            
            if src == dest:
                return messagebox.showerror("Error", "Source and destination cannot be same")
            
            amt = calc_fare(src, dest, cls, jt, qty)
            distance = calculate_distance(src, dest)
            
            if amt == 0:
                return messagebox.showerror("Error", "Invalid journey selection")
            
            # Confirm
            if not messagebox.askyesno("Confirm Booking", 
                f"Journey: {src} → {dest}\nDistance: ~{distance} km\nClass: {cls}\nType: {jt}\nPassengers: {qty}\n\nTotal Fare: ₹{amt:.2f}\n\nProceed to payment?"):
                return
            
            # OTP
            otp = generate_otp()
            messagebox.showinfo("Payment OTP", f"Your OTP: {otp}\n(Demo mode)")
            
            if not otp_window(self, otp):
                return messagebox.showinfo("Cancelled", "Booking cancelled")
            
            # Check balance
            if state.wallet < amt:
                return messagebox.showerror("Insufficient Balance", 
                    f"Wallet Balance: ₹{state.wallet:.2f}\nRequired: ₹{amt:.2f}\nShort by: ₹{amt - state.wallet:.2f}\n\nPlease add money to wallet.")
            
            # Book ticket
            state.wallet -= amt
            pnr = gen_pnr()
            txn_id = gen_txn_id()
            valid_until = get_validity(jt, distance)
            
            ticket = {
                "pnr": pnr,
                "txn_id": txn_id,
                "source": src,
                "destination": dest,
                "distance": distance,
                "class": cls,
                "journey_type": jt,
                "passengers": qty,
                "fare": amt,
                "booked_at": datetime.now(),
                "valid_until": valid_until,
                "status": "Active"
            }
            
            state.tickets.append(ticket)
            
            messagebox.showinfo("Booking Successful! 🎉", 
                f"Ticket Booked Successfully!\n\nPNR: {pnr}\nTransaction ID: {txn_id}\n\nJourney: {src} → {dest}\nDistance: ~{distance} km\nFare: ₹{amt:.2f}\n\nValid until: {valid_until.strftime('%d %b %Y, %I:%M %p')}\n\nBalance: ₹{state.wallet:.2f}")
            
            self.reset()
            self.controller.show("Tickets")
            
        except Exception as e:
            messagebox.showerror("Error", f"Booking failed: {str(e)}")

class Tickets(tk.Frame):
    def __init__(self, p, c):
        super().__init__(p, bg=BG)
        self.controller = c
        
        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=40, pady=30)
        
        header = tk.Frame(main, bg=BG)
        header.pack(fill="x", pady=20)
        
        tk.Label(header, text="📋 My Railway Tickets",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(side="left")
        
        tk.Button(header, text="🔄 Refresh",
                  bg=PRIMARY, fg=WHITE,
                  font=("Arial", 10, "bold"),
                  padx=15, pady=8,
                  command=self.refresh).pack(side="right")
        
        # Scrollable frame
        container = tk.Frame(main, bg=BG)
        container.pack(fill="both", expand=True)
        
        canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable = tk.Frame(canvas, bg=BG)
        
        self.scrollable.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def refresh(self):
        for widget in self.scrollable.winfo_children():
            widget.destroy()
        
        if not state.tickets:
            tk.Label(self.scrollable, 
                    text="📭 No tickets booked yet\n\nBook your first railway ticket to get started!",
                    font=("Arial", 14), bg=BG, fg="gray").pack(pady=50)
        else:
            for ticket in reversed(state.tickets):
                self.create_ticket_card(ticket)

    def create_ticket_card(self, t):
        card = tk.Frame(self.scrollable, bg=WHITE, relief="solid", bd=2)
        card.pack(fill="x", pady=10, padx=10)
        
        # Header
        hdr = tk.Frame(card, bg=PRIMARY)
        hdr.pack(fill="x")
        
        tk.Label(hdr, text=f"🎫 PNR: {t['pnr']}", font=("Arial", 13, "bold"),
                 bg=PRIMARY, fg=WHITE).pack(side="left", padx=15, pady=12)
        
        # Status
        now = datetime.now()
        if t['valid_until'] > now:
            status_text = "✓ Active"
            status_bg = SUCCESS
        else:
            status_text = "✗ Expired"
            status_bg = DANGER
        
        tk.Label(hdr, text=status_text, font=("Arial", 11, "bold"),
                 bg=status_bg, fg=WHITE, padx=12, pady=6).pack(side="right", padx=15)
        
        # Content
        content = tk.Frame(card, bg=WHITE)
        content.pack(fill="both", padx=20, pady=15)
        
        # Journey
        journey = tk.Frame(content, bg=WHITE)
        journey.pack(fill="x", pady=5)
        
        tk.Label(journey, text=f"🚉 {t['source']}",
                 font=("Arial", 14, "bold"), bg=WHITE).pack(side="left")
        
        tk.Label(journey, text="  →  ",
                 font=("Arial", 14), bg=WHITE, fg="gray").pack(side="left")
        
        tk.Label(journey, text=f"🎯 {t['destination']}",
                 font=("Arial", 14, "bold"), bg=WHITE).pack(side="left")
        
        # Details
        details = f"Class: {t['class']} | Type: {t['journey_type']} | Passengers: {t['passengers']} | Distance: ~{t['distance']} km"
        tk.Label(content, text=details,
                 font=("Arial", 10), bg=WHITE, fg="gray").pack(anchor="w", pady=5)
        
        tk.Label(content, text=f"💰 Fare: ₹{t['fare']:.2f}",
                 font=("Arial", 11, "bold"), bg=WHITE, fg=SUCCESS).pack(anchor="w", pady=5)
        
        # Times
        tk.Label(content,
                 text=f"📅 Booked: {t['booked_at'].strftime('%d %b %Y, %I:%M %p')}",
                 font=("Arial", 9), bg=WHITE, fg="gray").pack(anchor="w")
        
        tk.Label(content,
                 text=f"⏰ Valid until: {t['valid_until'].strftime('%d %b %Y, %I:%M %p')}",
                 font=("Arial", 9), bg=WHITE, fg="gray").pack(anchor="w")
        
        # Transaction
        tk.Label(content, text=f"Transaction ID: {t['txn_id']}",
                 font=("Arial", 8), bg=WHITE, fg="gray").pack(anchor="w", pady=(5, 0))

class Wallet(tk.Frame):
    def __init__(self, p, c):
        super().__init__(p, bg=BG)
        self.controller = c
        
        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=40, pady=30)
        
        tk.Label(main, text="💳 My Wallet",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(pady=20)
        
        # Balance
        balance = tk.Frame(main, bg=WHITE, relief="solid", bd=2)
        balance.pack(fill="x", pady=10)
        
        tk.Label(balance, text="Current Balance", font=("Arial", 13),
                 bg=WHITE, fg="gray").pack(pady=(20, 5))
        
        self.balance_lbl = tk.Label(balance, text="₹0.00", font=("Arial", 32, "bold"),
                                    bg=WHITE, fg=PRIMARY)
        self.balance_lbl.pack(pady=15)
        
        # Add money
        add = tk.Frame(main, bg=WHITE, relief="solid", bd=1)
        add.pack(fill="x", pady=20)
        
        tk.Label(add, text="➕ Add Money to Wallet", font=("Arial", 15, "bold"),
                 bg=WHITE, fg=DARK).pack(pady=15)
        
        amount_frame = tk.Frame(add, bg=WHITE)
        amount_frame.pack(pady=10)
        
        tk.Label(amount_frame, text="₹", font=("Arial", 16, "bold"),
                 bg=WHITE).pack(side="left", padx=5)
        
        self.amount = tk.Entry(amount_frame, font=("Arial", 15), width=15, justify="center")
        self.amount.pack(side="left")
        
        # Quick buttons
        tk.Label(add, text="Quick Add:", font=("Arial", 10),
                 bg=WHITE, fg="gray").pack(pady=(15, 5))
        
        quick = tk.Frame(add, bg=WHITE)
        quick.pack(pady=5)
        
        for amt in [100, 500, 1000, 2000, 5000]:
            tk.Button(quick, text=f"₹{amt}",
                     bg=LIGHT_GRAY, fg=DARK,
                     font=("Arial", 10, "bold"),
                     padx=15, pady=8,
                     command=lambda a=amt: self.set_amt(a)).pack(side="left", padx=5)
        
        tk.Button(add, text="💰 Add Money",
                  bg=SUCCESS, fg=WHITE,
                  font=("Arial", 13, "bold"),
                  padx=30, pady=15,
                  command=self.add_money).pack(pady=25)

    def set_amt(self, amt):
        self.amount.delete(0, tk.END)
        self.amount.insert(0, str(amt))

    def refresh(self):
        self.balance_lbl.config(text=f"₹{state.wallet:.2f}")

    def add_money(self):
        try:
            amt_str = self.amount.get().strip()
            
            if not amt_str:
                return messagebox.showerror("Error", "Please enter amount")
            
            if not amt_str.replace('.', '', 1).isdigit():
                return messagebox.showerror("Error", "Enter valid amount")
            
            amt = float(amt_str)
            
            if amt <= 0:
                return messagebox.showerror("Error", "Amount must be greater than zero")
            
            if amt > 50000:
                return messagebox.showerror("Error", "Maximum ₹50,000 per transaction")
            
            # OTP
            otp = generate_otp()
            messagebox.showinfo("Payment OTP", f"Your OTP: {otp}\n(Demo mode)")
            
            if not otp_window(self, otp):
                return messagebox.showinfo("Cancelled", "Transaction cancelled")
            
            state.wallet += amt
            txn_id = gen_txn_id()
            
            messagebox.showinfo("Success! 💰", 
                f"₹{amt:.2f} added successfully!\n\nTransaction ID: {txn_id}\nNew Balance: ₹{state.wallet:.2f}")
            
            self.amount.delete(0, tk.END)
            self.refresh()
            
        except Exception as e:
            messagebox.showerror("Error", f"Transaction failed: {str(e)}")

class Routes(tk.Frame):
    def __init__(self, p, c):
        super().__init__(p, bg=BG)
        self.controller = c

        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=40, pady=30)

        tk.Label(main, text="🗺️ Route Planner - Indian Railways",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(pady=20)

        form = tk.Frame(main, bg=WHITE, relief="solid", bd=1)
        form.pack(fill="x", pady=10)

        tk.Label(form, text="From", font=("Arial", 11, "bold"), bg=WHITE).grid(row=0, column=0, padx=10, pady=10)
        self.src = ttk.Combobox(form, values=get_all_stations(), state="readonly", width=30)
        self.src.grid(row=0, column=1, padx=10)

        tk.Label(form, text="To", font=("Arial", 11, "bold"), bg=WHITE).grid(row=1, column=0, padx=10, pady=10)
        self.dest = ttk.Combobox(form, values=get_all_stations(), state="readonly", width=30)
        self.dest.grid(row=1, column=1, padx=10)

        tk.Button(form, text="🔍 Show Route",
                  bg=PRIMARY, fg=WHITE,
                  font=("Arial", 11, "bold"),
                  padx=20, pady=8,
                  command=self.show_route).grid(row=2, column=0, columnspan=2, pady=15)

        # Output
        output_frame = tk.Frame(main, bg=WHITE, relief="solid", bd=1)
        output_frame.pack(fill="both", expand=True, pady=20)

        self.output = scrolledtext.ScrolledText(
            output_frame, height=15, font=("Arial", 10),
            wrap=tk.WORD, state="disabled"
        )
        self.output.pack(fill="both", expand=True, padx=15, pady=15)

    def show_route(self):
        src = self.src.get()
        dest = self.dest.get()

        if not src or not dest:
            return messagebox.showerror("Error", "Select both source and destination")

        if src == dest:
            return messagebox.showerror("Error", "Source and destination cannot be same")

        path = get_route_path(src, dest)
        distance = calculate_distance(src, dest)

        self.output.config(state="normal")
        self.output.delete(1.0, tk.END)

        self.output.insert(tk.END, f"🚉 Route: {src} → {dest}\n")
        self.output.insert(tk.END, f"📏 Approx Distance: {distance} km\n\n")
        self.output.insert(tk.END, "🛤️ Path:\n\n")

        for s in path:
            self.output.insert(tk.END, f"➡️ {s}\n")

        self.output.config(state="disabled")

    def refresh(self):
        pass


class AI(tk.Frame):
    def __init__(self, p, c):
        super().__init__(p, bg=BG)
        self.controller = c
        
        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=40, pady=30)
        
        tk.Label(main, text="🤖 AI Railway Assistant",
                 font=("Arial", 22, "bold"),
                 bg=BG, fg=DARK).pack(pady=20)
        
        # Chat
        chat_frame = tk.Frame(main, bg=WHITE, relief="solid", bd=1)
        chat_frame.pack(fill="both", expand=True)
        
        self.chat = scrolledtext.ScrolledText(chat_frame, height=20, font=("Arial", 10),
                                               wrap=tk.WORD, bg=WHITE, state="disabled")
        self.chat.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Input
        input_frame = tk.Frame(chat_frame, bg=WHITE)
        input_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        self.entry = tk.Entry(input_frame, font=("Arial", 11))
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind('<Return>', lambda e: self.ask())
        
        tk.Button(input_frame, text="📤 Send",
                  bg=PRIMARY, fg=WHITE,
                  font=("Arial", 11, "bold"),
                  padx=25, pady=10,
                  command=self.ask).pack(side="right")
        
        # Suggestions
        suggest_frame = tk.Frame(main, bg=LIGHT_GRAY, relief="solid", bd=1)
        suggest_frame.pack(fill="x", pady=(10, 0))
        
        tk.Label(suggest_frame, text="💡 Try asking:",
                 font=("Arial", 11, "bold"), bg=LIGHT_GRAY).pack(pady=10)
        
        suggestions = [
            "How many stations are there?",
            "What's the cheapest class?",
            "Tell me about Western line",
            "Show AC classes and fares"
        ]
        
        for s in suggestions:
            tk.Button(suggest_frame, text=f"• {s}",
                     bg=WHITE, fg=DARK,
                     font=("Arial", 9),
                     relief="flat",
                     anchor="w",
                     command=lambda q=s: self.ask_preset(q)).pack(fill="x", padx=10, pady=2)
        
        tk.Label(suggest_frame, text="", bg=LIGHT_GRAY).pack(pady=5)
        
        # Welcome
        self.add_msg("AI", "Hello! I'm your Indian Railways assistant. Ask me about stations, routes, fares, or booking!")

    def add_msg(self, sender, msg):
        self.chat.config(state="normal")
        timestamp = datetime.now().strftime("%H:%M")
        self.chat.insert(tk.END, f"\n[{timestamp}] {sender}: {msg}\n")
        self.chat.config(state="disabled")
        self.chat.see(tk.END)

    def ask_preset(self, q):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, q)
        self.ask()

    def ask(self):
        q = self.entry.get().strip()
        if not q:
            return
        
        self.add_msg("You", q)
        reply = ai_reply(q)
        self.add_msg("AI", reply)
        
        self.entry.delete(0, tk.END)

    def refresh(self):
        pass

# ==================================================
# RUN
# ==================================================
if __name__ == "__main__":
    Login().mainloop()