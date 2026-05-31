import sqlite3
import pandas as pd


def get_transaction_summary(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT
        SUM(transaction_count) as total_count,
        SUM(transaction_amount) as total_amount
    FROM aggregated_transaction
    WHERE year = {year}
    AND quarter = {quarter}
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result


def get_user_summary(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT
        SUM(registered_users) as total_users
    FROM aggregated_user
    WHERE year = {year}
    AND quarter = {quarter}
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result

def get_transaction_by_type(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT transaction_type,
           SUM(transaction_count) as total_count,
           SUM(transaction_amount) as total_amount
    FROM aggregated_transaction
    WHERE year = {year}
    AND quarter = {quarter}
    GROUP BY transaction_type
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result

def get_state_analysis(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT state,
           SUM(transaction_count) as total_count,
           SUM(transaction_amount) as total_amount
    FROM aggregated_transaction
    WHERE year = {year}
    AND quarter = {quarter}
    GROUP BY state
    ORDER BY total_amount DESC
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result

def get_top_users(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT state,
           SUM(registered_users) as total_users,
           SUM(app_opens) as total_app_opens
    FROM aggregated_user
    WHERE year = {year}
    AND quarter = {quarter}
    GROUP BY state
    ORDER BY total_users DESC
    LIMIT 10
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result

def get_transaction_trend(transaction_type):

    conn = sqlite3.connect("phonepe_pulse.db")

    if transaction_type == "All":

        query = """
        SELECT year,
               quarter,
               SUM(transaction_count) as total_count,
               SUM(transaction_amount) as total_amount
        FROM aggregated_transaction
        GROUP BY year, quarter
        ORDER BY year, quarter
        """

    else:

        query = f"""
        SELECT year,
               quarter,
               SUM(transaction_count) as total_count,
               SUM(transaction_amount) as total_amount
        FROM aggregated_transaction
        WHERE transaction_type = '{transaction_type}'
        GROUP BY year, quarter
        ORDER BY year, quarter
        """

    result = pd.read_sql(query, conn)

    conn.close()

    return result


def get_top_districts(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT entity_name,
           SUM(transaction_count) as total_count,
           SUM(transaction_amount) as total_amount
    FROM top_transaction
    WHERE year = {year}
    AND quarter = {quarter}
    AND entity_type = 'district'
    GROUP BY entity_name
    ORDER BY total_amount DESC
    LIMIT 10
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result


def get_user_engagement(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT state,
           SUM(registered_users) as total_users,
           SUM(app_opens) as total_app_opens
    FROM aggregated_user
    WHERE year = {year}
    AND quarter = {quarter}
    GROUP BY state
    ORDER BY total_users DESC
    LIMIT 15
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result

def get_top_state(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    query = f"""
    SELECT state,
           SUM(transaction_amount) as total_amount
    FROM aggregated_transaction
    WHERE year = {year}
    AND quarter = {quarter}
    GROUP BY state
    ORDER BY total_amount DESC
    LIMIT 5
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result


def get_state_growth(year, quarter):

    conn = sqlite3.connect("phonepe_pulse.db")

    previous_quarter = quarter - 1
    previous_year = year

    if previous_quarter == 0:
        previous_quarter = 4
        previous_year = year - 1

    query = f"""
    SELECT
        current.state,
        current.total_amount AS current_amount,
        previous.total_amount AS previous_amount,

        (
            (
                current.total_amount - previous.total_amount
            ) * 100.0
        ) / previous.total_amount AS growth_percentage

    FROM

    (
        SELECT
            state,
            SUM(transaction_amount) AS total_amount
        FROM aggregated_transaction
        WHERE year = {year}
        AND quarter = {quarter}
        GROUP BY state
    ) current

    JOIN

    (
        SELECT
            state,
            SUM(transaction_amount) AS total_amount
        FROM aggregated_transaction
        WHERE year = {previous_year}
        AND quarter = {previous_quarter}
        GROUP BY state
    ) previous

    ON current.state = previous.state

    ORDER BY growth_percentage DESC
    LIMIT 10
    """

    result = pd.read_sql(query, conn)

    conn.close()

    return result