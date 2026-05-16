import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

def draw_table(ax, x, y, title, columns, color, width=2.8):
    row_h = 0.35
    ax.add_patch(mpatches.FancyBboxPatch((x, y), width, row_h, boxstyle="round,pad=0.02", facecolor=color, edgecolor='white', linewidth=1.5))
    ax.text(x + width/2, y + row_h/2, title, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    for i, col in enumerate(columns):
        bg = '#ffffff' if i % 2 == 0 else '#f0f0f0'
        ax.add_patch(mpatches.FancyBboxPatch((x, y - (i+1)*row_h), width, row_h, boxstyle="round,pad=0.02", facecolor=bg, edgecolor='#cccccc', linewidth=0.5))
        ax.text(x + 0.15, y - (i+1)*row_h + row_h/2, col, ha='left', va='center', fontsize=7.5, color='#333333')

draw_table(ax, 4.5, 7.5, 'fact_rental', ['rental_id PK', 'date_key FK', 'customer_key FK', 'film_key FK', 'store_key FK', 'staff_key FK', 'rental_duration_days', 'is_late', 'late_days'], '#e74c3c')
draw_table(ax, 4.5, 2.8, 'fact_payment', ['payment_id PK', 'date_key FK', 'customer_key FK', 'staff_key FK', 'rental_id', 'amount'], '#e67e22')
draw_table(ax, 0.3, 9.2, 'dim_date', ['date_key PK', 'full_date', 'day', 'month', 'quarter', 'year', 'is_weekend'], '#2980b9')
draw_table(ax, 0.3, 5.5, 'dim_customer', ['customer_key PK', 'customer_id', 'full_name', 'email', 'city', 'country', 'active'], '#27ae60')
draw_table(ax, 0.3, 2.2, 'dim_store', ['store_key PK', 'store_id', 'address', 'city', 'country'], '#8e44ad')
draw_table(ax, 11.0, 9.2, 'dim_film', ['film_key PK', 'film_id', 'title', 'language', 'rental_rate', 'rating'], '#16a085')
draw_table(ax, 11.0, 5.8, 'dim_category', ['category_key PK', 'category_id', 'category_name'], '#d35400')
draw_table(ax, 11.0, 3.5, 'dim_staff', ['staff_key PK', 'staff_id', 'full_name', 'store_id'], '#c0392b')

plt.title('Movie Rental Data Warehouse - Star Schema', fontsize=14, fontweight='bold', color='#2c3e50')
plt.tight_layout()
plt.savefig(r'C:\Users\User\OneDrive\Desktop\movie_rental_dw\diagrams\star_schema.png', dpi=150, bbox_inches='tight')
plt.show()
print("الداياغرام اتحفظ!")