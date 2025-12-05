import pandas as pd
import json
from difflib import SequenceMatcher
from datetime import datetime

class AlumniChatbot:
    """Chatbot engine for alumni database queries"""
    
    def __init__(self, csv_path):
        """Initialize with CSV data"""
        self.csv_path = csv_path
        self.data = pd.read_csv(csv_path)
        self.columns = self.data.columns.tolist()
        self.build_index()
    
    def build_index(self):
        """Build searchable indexes for quick queries"""
        self.indexes = {}
        for col in self.columns:
            if self.data[col].dtype == 'object':
                unique_vals = self.data[col].dropna().unique().tolist()
                self.indexes[col] = unique_vals
    
    def get_columns(self):
        """Return column names"""
        return self.columns
    
    def process_query(self, user_message):
        """Process user query and return response"""
        user_message_lower = user_message.lower()
        
        # Count queries
        if any(word in user_message_lower for word in ['how many', 'count', 'total', 'number of']):
            return self.handle_count_query(user_message)
        
        # Filter queries
        if any(word in user_message_lower for word in ['where', 'find', 'show', 'list', 'filter', 'from']):
            return self.handle_filter_query(user_message)
        
        # Statistics queries
        if any(word in user_message_lower for word in ['statistics', 'stats', 'distribution', 'top', 'most']):
            return self.handle_stats_query(user_message)
        
        # General info
        if any(word in user_message_lower for word in ['what', 'who', 'information', 'about']):
            return self.handle_info_query(user_message)
        
        # Default response
        return self.generate_default_response(user_message)
    
    def handle_count_query(self, message):
        """Handle 'how many' type queries"""
        message_lower = message.lower()
        
        # General alumni count
        if any(word in message_lower for word in ['alumni', 'students', 'graduates']):
            count = len(self.data)
            return f"There are **{count}** alumni records in the database."
        
        # Count by specific column
        for col in self.columns:
            if col.lower() in message_lower:
                count = self.data[col].nunique()
                return f"There are **{count}** unique values in the **{col}** category."
        
        return f"Total alumni in database: **{len(self.data)}**"
    
    def handle_filter_query(self, message):
        """Handle filter/search queries"""
        message_lower = message.lower()
        results = self.data.copy()
        filters_applied = []
        
        # Try to extract column and value to filter
        for col in self.columns:
            col_lower = col.lower()
            if col_lower in message_lower:
                # Extract potential value after column name
                words = message_lower.split()
                col_idx = None
                for i, word in enumerate(words):
                    if col_lower in word:
                        col_idx = i
                        break
                
                if col_idx is not None and col_idx + 1 < len(words):
                    search_term = words[col_idx + 1]
                    # Find matching values
                    matching_values = [v for v in self.indexes.get(col, []) 
                                     if search_term in str(v).lower()]
                    
                    if matching_values:
                        results = results[results[col].isin(matching_values)]
                        filters_applied.append(f"{col}: {', '.join(map(str, matching_values[:3]))}")
        
        if filters_applied:
            result_count = len(results)
            response = f"Found **{result_count}** alumni matching your criteria:\n"
            response += "\n".join([f"- {f}" for f in filters_applied])
            
            if result_count > 0 and result_count <= 10:
                response += "\n\n**Results:**\n"
                for idx, row in results.head(10).iterrows():
                    response += f"\n{idx + 1}. " + " | ".join([f"**{col}**: {row[col]}" for col in self.columns[:3]])
            
            return response
        
        return "I couldn't find specific filters in your query. Could you be more specific? For example: 'Show alumni from 2020' or 'Find alumni working at Microsoft'"
    
    def handle_stats_query(self, message):
        """Handle statistics queries"""
        message_lower = message.lower()
        response = ""
        
        # Distribution queries
        if 'distribution' in message_lower:
            for col in self.columns:
                if col.lower() in message_lower:
                    dist = self.data[col].value_counts().head(5)
                    response = f"**Distribution of {col}:**\n"
                    for val, count in dist.items():
                        response += f"- {val}: {count}\n"
                    return response
        
        # Top queries
        if 'top' in message_lower:
            for col in self.columns:
                if col.lower() in message_lower:
                    top = self.data[col].value_counts().head(5)
                    response = f"**Top 5 {col}:**\n"
                    for val, count in top.items():
                        response += f"- {val}: {count} alumni\n"
                    return response
        
        # Most common
        if 'most' in message_lower and 'common' in message_lower:
            for col in self.columns:
                if col.lower() in message_lower:
                    most = self.data[col].value_counts().head(1)
                    return f"The most common {col} is **{most.index[0]}** with {most.values[0]} alumni."
        
        return self.get_stats()
    
    def handle_info_query(self, message):
        """Handle general information queries"""
        return f"""**Alumni Database Information:**
- Total Records: {len(self.data)}
- Columns: {', '.join(self.columns)}
- Database Fields: {len(self.columns)}

You can ask me questions like:
- "How many alumni are there?"
- "Show me alumni from 2020"
- "What companies do alumni work at?"
- "Distribution of alumni by branch"
"""
    
    def generate_default_response(self, message):
        """Generate response for unrecognized queries"""
        return """I didn't quite understand that. Here are some things I can help with:

**Count Queries:** "How many alumni are there?"
**Filter Queries:** "Show alumni from 2020" or "Find alumni working at Google"
**Statistics:** "Top companies" or "Distribution by branch"
**Information:** "What's in the database?"

Please try rephrasing your question or use one of the suggestions above."""
    
    def get_stats(self):
        """Get overall database statistics"""
        stats = {
            'total_records': len(self.data),
            'total_columns': len(self.columns),
            'columns': self.columns,
            'memory_usage': self.data.memory_usage(deep=True).sum() / 1024 / 1024,  # MB
        }
        
        # Add column-specific stats
        for col in self.columns[:5]:  # Top 5 columns
            if self.data[col].dtype == 'object':
                stats[col] = {
                    'unique_values': self.data[col].nunique(),
                    'top_values': self.data[col].value_counts().head(3).to_dict()
                }
        
        return stats
