import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------------------------------------------------------
# 1. PAGE CONFIG & ELECTRIC DEEP BLUE GLASSMORPHISM STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="DelusionCheck | Reality Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """ 
    <style> 
    /* Original Deep Electric Blue & Midnight Gradient Background */ 
    .stApp { 
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 40%, #0F2744 70%, #0284C7 100%) !important; 
        color: #F8FAFC !important; 
    } 
    
    /* Base Text Styling */
    p, span, label, div {
        color: #E2E8F0 !important;
        font-weight: 500;
    }

    /* Input Labels - Glowing Cyan Accent */
    .stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label {
        color: #38BDF8 !important; 
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }
    
    /* Input Fields - Translucent Dark Frosted Glass */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: rgba(15, 23, 42, 0.75) !important;
        border: 1px solid rgba(56, 189, 248, 0.4) !important;
        color: #F8FAFC !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="popover"] div {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
    }

    ul[role="listbox"] li {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    
    ul[role="listbox"] li:hover {
        background-color: #1E293B !important;
    }
     
    /* Header Gradient Title */ 
    .main-header { 
        font-size: 3.4rem !important; 
        background: linear-gradient(135deg, #38BDF8, #818CF8, #C084FC); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-weight: 900; 
        text-align: center; 
        letter-spacing: -1px; 
        margin-bottom: 0px; 
    } 
    .sub-header { 
        font-size: 1.15rem; 
        color: #94A3B8 !important; 
        text-align: center; 
        margin-bottom: 25px; 
        font-weight: 500;
    } 
     
    /* STREAMLIT CONTAINER FROSTED GLASS CARDS */
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background: rgba(15, 23, 42, 0.55) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
        border-radius: 24px !important;
        padding: 24px !important;
    }

    /* AESTHETIC EMOJI GLASS CASE BADGES */
    .glass-badge-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
    }
    .emoji-glass-case {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 46px;
        height: 46px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 14px;
        font-size: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }
    .glass-badge-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #F8FAFC !important;
        margin: 0;
    }

    /* Glowing Action Button */ 
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(90deg, #0284C7, #6366F1, #A855F7) !important; 
        color: white !important; 
        font-size: 1.2rem !important; 
        font-weight: 800 !important; 
        border-radius: 14px !important; 
        border: none !important; 
        padding: 0.85rem 1.5rem !important; 
        box-shadow: 0 4px 25px rgba(99, 102, 241, 0.45) !important; 
        transition: all 0.3s ease-in-out !important; 
    } 
    .stButton>button:hover { 
        transform: translateY(-2px) scale(1.01) !important; 
        box-shadow: 0 6px 30px rgba(168, 85, 247, 0.65) !important; 
    } 
     
    /* Sidebar Styling */ 
    section[data-testid="stSidebar"] { 
        background-color: rgba(15, 23, 42, 0.85) !important; 
        border-right: 1px solid rgba(255, 255, 255, 0.08); 
    } 

    /* Creator & Preview Glass Boxes */
    .creator-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 16px;
        padding: 16px;
        margin-top: 10px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .creator-box p {
        color: #CBD5E1 !important;
        font-size: 0.95rem;
    }

    .preview-box {
        background-color: rgba(255, 255, 255, 0.04);
        border: 1px dashed rgba(56, 189, 248, 0.5);
        border-radius: 12px;
        padding: 12px;
        margin-top: 15px;
    }
    </style> 
""",
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# 2. TAX & INFLATION ENGINE
# -----------------------------------------------------------------------------
def calculate_indian_income_tax(gross_salary):
    standard_deduction = 75000
    taxable_income = max(0, gross_salary - standard_deduction)

    if taxable_income <= 700000:
        return 0.0

    tax = 0.0
    slabs = [
        (300000, 0.00),
        (400000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (200000, 0.20),
        (float("inf"), 0.30),
    ]

    temp_income = taxable_income
    for limit, rate in slabs:
        if temp_income > 0:
            taxable_in_slab = min(temp_income, limit)
            tax += taxable_in_slab * rate
            temp_income -= taxable_in_slab
        else:
            break

    return tax * 1.04


def calculate_required_gross_salary(target_net_takehome):
    low, high = target_net_takehome, target_net_takehome * 2.5
    for _ in range(50):
        mid = (low + high) / 2
        net = mid - calculate_indian_income_tax(mid)
        if net < target_net_takehome:
            low = mid
        else:
            high = mid
    return mid


# -----------------------------------------------------------------------------
# 3. HEADER
# -----------------------------------------------------------------------------
st.markdown(
    '<div class="main-header">DelusionCheck 💀</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-header">Why did the bicycle fall over? Because it was two-tired. Why did your budget fall over? Let\'s do the math and find out.</div>',
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 4. SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
    <div class="glass-badge-header">
        <div class="emoji-glass-case">💡</div>
        <div class="glass-badge-title">Simple Dictionary</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    * **CTC:** Cost To Company. Total money spent on you. It sounds big until taxes chop it down. I tried telling a joke about taxes once, but 30% of it got taken away.
    * **In-Hand Salary:** The actual cash landing in your bank account every month.
    * **Inflation:** Why a book or album costs more every single year. It's un-book-lievable.
    """
    )

    st.markdown("---")

    st.markdown(
        """
    <div class="glass-badge-header">
        <div class="emoji-glass-case">⚙️</div>
        <div class="glass-badge-title">Time Machine</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    cpi_inflation = st.slider(
        "Expected Yearly Inflation (%):",
        3.0,
        10.0,
        6.0,
        step=0.5,
    )
    years_future = st.slider(
        "Years until you start your job:", 1, 10, 4
    )

    st.markdown("---")

    st.markdown(
        """
    <div class="creator-box">
        <div class="glass-badge-header">
            <div class="emoji-glass-case">🎧</div>
            <div class="glass-badge-title" style="color:#38BDF8 !important; font-size:1.1rem;">About The Creator</div>
        </div>
        <p>Hi, I'm <b>an 11th grade Commerce student</b> whose brain is fueled by a chaotic mix of Stray Kids, stacks of unread books, and terribly dry dad jokes.</p>
        <p>I built <b>DelusionCheck</b> after hearing people talk about starting packages like ₹20 LPA as if it's infinite money—without realizing taxes, rent, and inflation will leave their bank accounts feeling <i>two-tired</i> real quick.</p>
        <p><i>"I'm reading a book on anti-gravity... I just can't put it down."</i> 📖✨</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# 5. INPUT FORM (WITH EMOJI GLASS CASE HEADERS)
# -----------------------------------------------------------------------------
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    with st.container(border=True):
        st.markdown(
            """
        <div class="glass-badge-header">
            <div class="emoji-glass-case">🏠</div>
            <div class="glass-badge-title">1. Your Dream Lifestyle</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        city = st.selectbox(
            "Which city vibe are you going for?",
            [
                "Mumbai / BKC (Very Expensive)",
                "Gurgaon / Delhi NCR (High Cost)",
                "Bengaluru (High Rent & Deposits)",
                "Pune / Hyderabad / Tier-2 City (Moderate)",
                "International City (NYC / London - Pure Flex)",
            ],
        )
        city_mult = (
            1.6
            if "Mumbai" in city
            else (
                1.4
                if "Gurgaon" in city or "Bengaluru" in city
                else (1.0 if "Pune" in city else 3.8)
            )
        )

        custom_location = st.text_input(
            "Type your exact dream neighborhood or area:",
            value="Bandra West, Mumbai",
        )

        rent = st.slider(
            "Monthly Rent / Living Cost (₹):", 15000, 250000, 45000, step=5000
        )

        dining_cost = st.slider(
            "Monthly Food, Outings, Books & Album Drops (₹):",
            min_value=5000,
            max_value=100000,
            value=20000,
            step=2500,
        )

        transit_cost = st.slider(
            "Monthly Travel / Vehicle Costs (₹):",
            min_value=2000,
            max_value=100000,
            value=15000,
            step=1000,
        )

        savings_percent = st.slider(
            "How much of your income do you plan to SAVE? (%):",
            min_value=0,
            max_value=50,
            value=20,
            step=5,
        )

        custom_vacation = st.text_input(
            "Type your dream annual vacation:",
            value="SKZ World Tour & 2 Weeks in Japan 🇯🇵",
        )

        vacations = st.slider(
            "Yearly Vacation Budget (₹):",
            25000,
            1500000,
            200000,
            step=25000,
        )

        st.markdown(
            f"""
        <div class="preview-box">
            <p style="margin:0; font-size:0.9rem; color:#38BDF8;">✨ <b>Live Vibe Check:</b></p>
            <p style="margin:4px 0 0 0; color:#E2E8F0;">Living in <b>{custom_location}</b> | Vacation: <b>{custom_vacation}</b> | Saving: <b>{savings_percent}%</b></p>
        </div>
        """,
            unsafe_allow_html=True,
        )

with col_right:
    with st.container(border=True):
        st.markdown(
            """
        <div class="glass-badge-header">
            <div class="emoji-glass-case">💼</div>
            <div class="glass-badge-title">2. Your Job & Expected Salary</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        field = st.selectbox(
            "Target Career Field:",
            [
                "Investment Banking / Finance",
                "Software Development / AI",
                "Management Consulting",
                "Corporate Law",
                "Marketing & Media",
                "Government / Teaching",
            ],
        )

        expected_ctc = st.number_input(
            "Expected Starting Package / Total Yearly Salary (₹):",
            value=1200000,
            step=50000,
        )

        st.markdown("<br><br>", unsafe_allow_html=True)
        run_btn = st.button("🔥 RUN THE REALITY CHECK ENGINE")

# -----------------------------------------------------------------------------
# 6. ENGINE OUTPUT & ROASTS
# -----------------------------------------------------------------------------
if run_btn:
    living_cost_monthly = (
        rent + dining_cost + transit_cost + (vacations / 12)
    ) * city_mult

    savings_factor = 1 / (1 - (savings_percent / 100))
    total_net_monthly_needed = living_cost_monthly * savings_factor

    inflated_monthly_exp = total_net_monthly_needed * (
        (1 + (cpi_inflation / 100)) ** years_future
    )
    annual_net_needed = inflated_monthly_exp * 12
    required_gross_ctc = calculate_required_gross_salary(annual_net_needed)

    gap = required_gross_ctc - expected_ctc
    delusion_score = (
        0 if gap <= 0 else min(100, int((gap / required_gross_ctc) * 100))
    )

    st.markdown("---")

    if delusion_score == 0:
        avatar_reaction = "🧠 S-Class Math Genius!"
        roast_text = f"Why did your bank account smile? Because it actually fits your budget! Living in {custom_location}, trip to {custom_vacation}, and saving {savings_percent}% works out cleanly."
        alert_color = "#38BDF8"
    elif delusion_score < 35:
        avatar_reaction = "🚲 Two-Tired Budget Alert!"
        roast_text = f"Why did the budget fall over? Because after taxes, living in {custom_location} and going to {custom_vacation} made it two-tired! You're slightly optimistic."
        alert_color = "#F59E0B"
    elif delusion_score < 70:
        avatar_reaction = "📖 Out of Fiction Books Level"
        roast_text = f"I love fiction, but expecting this salary to cover {custom_location}, '{custom_vacation}', AND {savings_percent}% savings is a plot twist no author could pull off."
        alert_color = "#F43F5E"
    else:
        avatar_reaction = "🤡 Pure Unhinged Fantasy"
        roast_text = f"Living in {custom_location} + '{custom_vacation}' + saving {savings_percent}% on this package? Math didn't just fall over, it packed its bags and left the building. 😂"
        alert_color = "#E11D48"

    m1, m2, m3 = st.columns(3)
    m1.metric(
        "Monthly Cash Needed In Bank", f"₹{int(inflated_monthly_exp):,}"
    )
    m2.metric(
        "Pre-Tax Package (CTC) Needed", f"₹{int(required_gross_ctc):,}"
    )
    m3.metric("Your Expected Package", f"₹{int(expected_ctc):,}")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f'<h2 style="text-align: center; color: {alert_color};">{avatar_reaction}</h2>',
        unsafe_allow_html=True,
    )
    st.progress(delusion_score / 100)
    st.markdown(
        f'<p style="text-align: center; font-size: 1.15rem; color: #94A3B8;"><i>"{roast_text}"</i></p>',
        unsafe_allow_html=True,
    )

    if delusion_score == 0:
        st.balloons()

    st.markdown("---")
    res_col1, res_col2 = st.columns([1, 1])

    with res_col1:
        with st.container(border=True):
            st.markdown(
                """
            <div class="glass-badge-header">
                <div class="emoji-glass-case">📊</div>
                <div class="glass-badge-title">Where Your Money Goes</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            savings_monthly = total_net_monthly_needed - living_cost_monthly

            labels = [
                "Rent",
                "Food, Books & Outings",
                "Travel",
                "Vacations",
                "Savings & Investments",
            ]
            sizes = [
                rent * city_mult,
                dining_cost * city_mult,
                transit_cost * city_mult,
                (vacations / 12) * city_mult,
                savings_monthly * city_mult,
            ]

            fig, ax = plt.subplots(figsize=(5, 5))
            fig.patch.set_facecolor("#0F172A")
            ax.set_facecolor("#0F172A")
            colors = ["#F43F5E", "#F59E0B", "#10B981", "#38BDF8", "#A855F7"]

            wedges, texts, autotexts = ax.pie(
                sizes,
                labels=labels,
                autopct="%1.1f%%",
                colors=colors,
                startangle=140,
                textprops={"color": "#F8FAFC", "weight": "bold"},
            )
            ax.axis("equal")
            st.pyplot(fig)

    with res_col2:
        with st.container(border=True):
            st.markdown(
                """
            <div class="glass-badge-header">
                <div class="emoji-glass-case">📲</div>
                <div class="glass-badge-title">Shareable Reality Card</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f""" 
            <div style="background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(12px); padding: 25px; border-radius: 18px; color: #F8FAFC; border: 1.5px solid {alert_color}; box-shadow: 0 8px 32px rgba(0,0,0,0.4);"> 
                <h3 style="color: {alert_color}; margin-top:0;">💀 DELUSIONCHECK REALITY CARD</h3> 
                <p style="color:#E2E8F0;"><b>Career Goal:</b> {field}</p> 
                <p style="color:#E2E8F0;"><b>Living Spot:</b> {custom_location}</p> 
                <p style="color:#E2E8F0;"><b>Dream Trip:</b> {custom_vacation}</p> 
                <p style="color:#E2E8F0;"><b>Savings Target:</b> {savings_percent}% of Income</p> 
                <p style="color:#E2E8F0;"><b>Expected Package:</b> ₹{int(expected_ctc):,}</p> 
                <p style="color:#E2E8F0;"><b>Real Package Needed:</b> ₹{int(required_gross_ctc):,}</p> 
                <hr style="border-color: rgba(255, 255, 255, 0.1);"> 
                <h2 style="color: {alert_color}; text-align: center; font-size: 2.2rem;">{delusion_score}% DELUSIONAL</h2> 
                <p style="text-align: center; font-size: 0.85rem; color: #38BDF8;">Created by an 11th Grade Commerce Student (Dad Joke & Book Lover Certified)</p> 
            </div> 
            """,
                unsafe_allow_html=True,
            )
            st.caption("📸 Screenshot this card and send it to your group chat!")

# Footer
st.markdown("---")
st.caption(
    "DelusionCheck v3.3 | Commerce & Financial Literacy Initiative | Built with Python & Streamlit"
)